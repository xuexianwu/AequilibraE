"""
 -----------------------------------------------------------------------------------------------------------
 Package:    AequilibraE

 Name:       Main interface for comparing assignment scenarios
 Purpose:    Load GUI and user interface for the scenario comparison procedure

 Original Author:  Pedro Camargo (c@margo.co)
 Contributors:
 Last edited by: Pedro Camargo

 Website:    www.AequilibraE.com
 Repository:  https://github.com/AequilibraE/AequilibraE

 Created:    2016-12-01
 Updated:
 Copyright:   (c) AequilibraE authors
 Licence:     See LICENSE.TXT
 -----------------------------------------------------------------------------------------------------------
 """

import qgis
from functools import partial
from qgis.core import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.gui import QgsMapLayerProxyModel
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from global_parameters import *
from random import randint

from forms import Ui_compare_scenarios
from auxiliary_functions import *


class CompareScenariosDialog(QDialog, Ui_compare_scenarios):
    def __init__(self, iface):
        QDialog.__init__(self)
        self.iface = iface
        self.setupUi(self)

        self.common_colour = "0, 0, 0, 255"
        self.positive_color = "0, 174, 116, 255"
        self.negative_color = "218, 0, 3, 255"

        self.band_size = 10.0
        self.space_size = 0.01
        self.layer = None
        self.drive_side = get_parameter_chain(['system', 'driving side'])

        # layers and fields        # For adding skims
        self.mMapLayerComboBox.setFilters(QgsMapLayerProxyModel.LineLayer)
        self.mMapLayerComboBox.layerChanged.connect(self.add_fields_to_cboxes)

        self.ab_FieldComboBoxBase.currentIndexChanged.connect(partial(self.choose_a_field, 'base_AB'))
        self.ba_FieldComboBoxBase.currentIndexChanged.connect(partial(self.choose_a_field, 'base_BA'))

        self.ab_FieldComboBoxAlt.currentIndexChanged.connect(partial(self.choose_a_field, 'alt_AB'))
        self.ba_FieldComboBoxAlt.currentIndexChanged.connect(partial(self.choose_a_field, 'alt_BA'))

        # space slider
        self.slider_spacer.setMinimum(1)
        self.slider_spacer.setMaximum(30)
        self.slider_spacer.setValue(1)
        self.slider_spacer.setTickPosition(QSlider.TicksBelow)
        self.slider_spacer.setTickInterval(10)
        self.slider_spacer.valueChanged.connect(self.spacevaluechange)

        # band slider
        self.slider_band_size.setMinimum(5)
        self.slider_band_size.setMaximum(150)
        self.slider_band_size.setValue(50)
        self.slider_band_size.setTickPosition(QSlider.TicksBelow)
        self.slider_band_size.setTickInterval(5)
        self.slider_band_size.valueChanged.connect(self.sizevaluechange)

        self.but_run.clicked.connect(self.execute_comparison)
        self.add_fields_to_cboxes()
        self.sizevaluechange()
        self.spacevaluechange()
        self.set_initial_value_if_available()

    def choose_a_field(self, modified):
        if modified[0:3] == 'bas':
            self.choose_field_indeed(modified, self.ab_FieldComboBoxBase, self.ba_FieldComboBoxBase)
        else:
            self.choose_field_indeed(modified, self.ab_FieldComboBoxAlt, self.ba_FieldComboBoxAlt)

    def choose_field_indeed(self, modified, ab, ba):
        i, j = 'AB', 'BA'
        text = ab.currentText()
        if i in text:
            text = text.replace(i, j)
            index = ba.findText(text, Qt.MatchFixedString)
            if index >= 0:
                ba.setCurrentIndex(index)
        if modified == j:
            text = ba.currentText()
            if j in text:
                text = text.replace(j, i)
                index = ab.findText(text, Qt.MatchFixedString)
                if index >= 0:
                    ab.setCurrentIndex(index)

    def set_initial_value_if_available(self):
        all_items = [self.ab_FieldComboBoxBase.itemText(i) for i in range(self.ab_FieldComboBoxBase.count())]

        for i in all_items:
            if 'AB' in i:
                index = self.ab_FieldComboBoxBase.findText(i, Qt.MatchFixedString)
                if index >= 0:
                    self.ab_FieldComboBoxBase.setCurrentIndex(index)
                    self.ab_FieldComboBoxAlt.setCurrentIndex(index)
                break

    def spacevaluechange(self):
        self.space_size = self.slider_spacer.value() / 100.0
        self.lbl_space.setText("{:3,.2f}".format(self.space_size))

    def sizevaluechange(self):
        self.band_size = self.slider_band_size.value() / 5.0
        self.lbl_width.setText("{:3,.2f}".format(self.band_size))

    def add_fields_to_cboxes(self):
        self.layer = get_vector_layer_by_name(self.mMapLayerComboBox.currentText())
        self.ab_FieldComboBoxBase.setLayer(self.layer)
        self.ba_FieldComboBoxBase.setLayer(self.layer)
        self.ab_FieldComboBoxAlt.setLayer(self.layer)
        self.ba_FieldComboBoxAlt.setLayer(self.layer)


    def execute_comparison(self):
        if self.check_inputs():
            self.but_run.setEnabled(False)
            self.band_size = str(self.band_size)
            self.space_size = str(self.space_size)

            # define the side of the plotting based on the side of the road the system has defined
            ab = -1
            if self.drive_side == 'right':
                ab = 1
            ba = - ab

            # fields
            ab_base = self.ab_FieldComboBoxBase.currentText()
            ba_base = self.ba_FieldComboBoxBase.currentText()
            ab_alt = self.ab_FieldComboBoxAlt.currentText()
            ba_alt = self.ba_FieldComboBoxAlt.currentText()
            idx_ab = self.layer.fieldNameIndex(ab_base)
            idx_ba = self.layer.fieldNameIndex(ba_base)
            idx2_ab = self.layer.fieldNameIndex(ab_alt)
            idx2_ba = self.layer.fieldNameIndex(ba_alt)

            # Create the bandwidths for the comon flow, if requested
            if self.radio_compo.isChecked():
                values = []
                values.append(self.layer.maximumValue(idx_ab))
                values.append(self.layer.maximumValue(idx_ba))
                values.append(self.layer.maximumValue(idx2_ab))
                values.append(self.layer.maximumValue(idx2_ba))
                max_value = max(values)

                # We create the styles for AB and BA directions and add to the fields
                for abb, aba, di, t in ([ab_base, ab_alt, ab, 'ab'],[ba_base, ba_alt, ba, 'ba']):
                    width = '(coalesce(scale_linear(min("' + abb + '","' + aba + '") , 0,' + str(max_value) + ', 0, ' + self.band_size + '), 0))'
                    offset = str(di) + '*(' + width + '/2 + ' + self.space_size + ')'
                    symbol_layer = self.create_style(width, offset, self.common_colour)
                    self.layer.rendererV2().symbol().appendSymbolLayer(symbol_layer)
                    if t == 'ab':
                        ab_offset = str(di) + '*(' + width + ' + ' + self.space_size + ')'
                    else:
                        ba_offset = str(di) + '*(' + width + ' + ' + self.space_size + ')'


            # If we want a plot of the differences only
            if self.radio_diff.isChecked():
                # we compute the size of the differences
                diffs = []
                for feat in self.layer.getFeatures():
                    diffs.append(abs(feat.attributes()[idx_ab] - feat.attributes()[idx2_ab]))
                    diffs.append(abs(feat.attributes()[idx_ba] - feat.attributes()[idx2_ba]))
                max_value = max(diffs)
                ab_offset = '0'
                ba_offset = '0'

            # We now create the positive and negative bandwidths for each side of the link
            styles = []
            styles.append((ab_base, ab_alt, self.positive_color, ab, ab_offset))
            styles.append((ab_alt, ab_base, self.negative_color, ab, ab_offset))
            styles.append((ba_base, ba_alt, self.positive_color, ba, ba_offset))
            styles.append((ba_alt, ba_base, self.negative_color, ba, ba_offset))

            for i in styles:
                width = '(coalesce(scale_linear(max("' + i[0] + '"-"' + i[1] + '",0) , 0,' + str(max_value) + ', 0, ' + self.band_size + '), 0))'
                offset = i[4] + '+' + str(i[3]) + '*(' + width + '/2 + ' + self.space_size + ')'
                symbol_layer = self.create_style(width, offset, i[2])
                self.layer.rendererV2().symbol().appendSymbolLayer(symbol_layer)

            self.layer.triggerRepaint()
            self.exit_procedure()

    def check_inputs(self):
        if self.layer is None:
            return False
        if min(self.ab_FieldComboBoxBase.currentIndex(), self.ba_FieldComboBoxBase.currentIndex(),
               self.ab_FieldComboBoxAlt.currentIndex(), self.ba_FieldComboBoxAlt.currentIndex()) < 0:
            return False
        return True

    def create_style(self, width, offset, color):
        symbol_layer = QgsSimpleLineSymbolLayerV2.create({})
        props = symbol_layer.properties()
        props['width_dd_expression'] = width
        props['offset_dd_expression'] = offset

        props['line_color'] = color
        symbol_layer = QgsSimpleLineSymbolLayerV2.create(props)
        return symbol_layer

    def exit_procedure(self):
        self.close()


if __name__ == '__main__':
    main()