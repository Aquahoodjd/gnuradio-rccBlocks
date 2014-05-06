#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Static RF or Single Path Rayleigh Faded RF
# Author: Richard Clarke
# Description: Provides either static RF or single path Rayleigh faded RF at specified doppler spread
# Generated: Thu Feb 20 01:35:28 2014
##################################################

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from optparse import OptionParser
from random import randint
import PyQt4.Qwt5 as Qwt
import SimpleXMLRPCServer
import rccBlocks
import sys
import threading
import time

class e100_fading_vaunix_qtgui(gr.top_block, Qt.QWidget):

	def __init__(self):
		gr.top_block.__init__(self, "Static RF or Single Path Rayleigh Faded RF")
		Qt.QWidget.__init__(self)
		self.setWindowTitle("Static RF or Single Path Rayleigh Faded RF")
		self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
		self.top_scroll_layout = Qt.QVBoxLayout()
		self.setLayout(self.top_scroll_layout)
		self.top_scroll = Qt.QScrollArea()
		self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
		self.top_scroll_layout.addWidget(self.top_scroll)
		self.top_scroll.setWidgetResizable(True)
		self.top_widget = Qt.QWidget()
		self.top_scroll.setWidget(self.top_widget)
		self.top_layout = Qt.QVBoxLayout(self.top_widget)
		self.top_grid_layout = Qt.QGridLayout()
		self.top_layout.addLayout(self.top_grid_layout)


		##################################################
		# Variables
		##################################################
		self.usrpRate = usrpRate = 250e3
		self.fd = fd = 50
		self.fdTs = fdTs = fd*(1.0/usrpRate)
		self.fadeMode = fadeMode = False
		self.centreFreq = centreFreq = 1e6
		self.baseband_multiplier = baseband_multiplier = 0.25
		self.atten = atten = 0

		##################################################
		# Blocks
		##################################################
		_fadeMode_check_box = Qt.QCheckBox("Fading Enabled")
		self._fadeMode_choices = {True: True, False: False}
		self._fadeMode_choices_inv = dict((v,k) for k,v in self._fadeMode_choices.iteritems())
		self._fadeMode_callback = lambda i: _fadeMode_check_box.setChecked(self._fadeMode_choices_inv[i])
		self._fadeMode_callback(self.fadeMode)
		_fadeMode_check_box.stateChanged.connect(lambda i: self.set_fadeMode(self._fadeMode_choices[bool(i)]))
		self.top_layout.addWidget(_fadeMode_check_box)
		self._atten_layout = Qt.QVBoxLayout()
		self._atten_tool_bar = Qt.QToolBar(self)
		self._atten_layout.addWidget(self._atten_tool_bar)
		self._atten_tool_bar.addWidget(Qt.QLabel("RF Attenuator Setting, dB"+": "))
		self._atten_counter = Qwt.QwtCounter()
		self._atten_counter.setRange(0, 63, 0.5)
		self._atten_counter.setNumButtons(2)
		self._atten_counter.setValue(self.atten)
		self._atten_tool_bar.addWidget(self._atten_counter)
		self._atten_counter.valueChanged.connect(self.set_atten)
		self._atten_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
		self._atten_slider.setRange(0, 63, 0.5)
		self._atten_slider.setValue(self.atten)
		self._atten_slider.setMinimumWidth(200)
		self._atten_slider.valueChanged.connect(self.set_atten)
		self._atten_layout.addWidget(self._atten_slider)
		self.top_layout.addLayout(self._atten_layout)
		self.xmlrpc_server_0 = SimpleXMLRPCServer.SimpleXMLRPCServer(("0.0.0.0", 1234), allow_none=True)
		self.xmlrpc_server_0.register_instance(self)
		threading.Thread(target=self.xmlrpc_server_0.serve_forever).start()
		self.uhd_usrp_sink_0_0_0 = uhd.usrp_sink(
			device_addr="",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_sink_0_0_0.set_subdev_spec("A:AB", 0)
		self.uhd_usrp_sink_0_0_0.set_samp_rate(usrpRate)
		self.uhd_usrp_sink_0_0_0.set_center_freq(centreFreq, 0)
		self.uhd_usrp_sink_0_0_0.set_gain(0, 0)
		self.rccBlocks_channelModel_cc_0 = rccBlocks.channelModel_cc(randint(-10000,0), fdTs, 1.0, False, fadeMode)
		self.rccBlocks_VNXLabBrick_0 = rccBlocks.VNXLabBrick(atten)
		self._fd_tool_bar = Qt.QToolBar(self)
		self._fd_tool_bar.addWidget(Qt.QLabel("Doppler Rate, Hz"+": "))
		self._fd_line_edit = Qt.QLineEdit(str(self.fd))
		self._fd_tool_bar.addWidget(self._fd_line_edit)
		self._fd_line_edit.returnPressed.connect(
			lambda: self.set_fd(eng_notation.str_to_num(self._fd_line_edit.text().toAscii())))
		self.top_layout.addWidget(self._fd_tool_bar)
		self.const_source_x_0_0 = gr.sig_source_f(0, gr.GR_CONST_WAVE, 0, 0, 1.0)
		self.const_source_x_0 = gr.sig_source_c(0, gr.GR_CONST_WAVE, 0, 0, 1.0+1j)
		self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, usrpRate)
		self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc((baseband_multiplier, ))

		##################################################
		# Connections
		##################################################
		self.connect((self.const_source_x_0, 0), (self.rccBlocks_channelModel_cc_0, 0))
		self.connect((self.blocks_multiply_const_vxx_1, 0), (self.uhd_usrp_sink_0_0_0, 0))
		self.connect((self.const_source_x_0_0, 0), (self.blocks_throttle_0, 0))
		self.connect((self.blocks_throttle_0, 0), (self.rccBlocks_VNXLabBrick_0, 0))
		self.connect((self.rccBlocks_channelModel_cc_0, 0), (self.blocks_multiply_const_vxx_1, 0))


	def get_usrpRate(self):
		return self.usrpRate

	def set_usrpRate(self, usrpRate):
		self.usrpRate = usrpRate
		self.set_fdTs(self.fd*(1.0/self.usrpRate))
		self.blocks_throttle_0.set_sample_rate(self.usrpRate)
		self.uhd_usrp_sink_0_0_0.set_samp_rate(self.usrpRate)

	def get_fd(self):
		return self.fd

	def set_fd(self, fd):
		self.fd = fd
		self.set_fdTs(self.fd*(1.0/self.usrpRate))
		self._fd_line_edit.setText(eng_notation.num_to_str(self.fd))

	def get_fdTs(self):
		return self.fdTs

	def set_fdTs(self, fdTs):
		self.fdTs = fdTs
		self.rccBlocks_channelModel_cc_0.set_dopplerFreq(self.fdTs)

	def get_fadeMode(self):
		return self.fadeMode

	def set_fadeMode(self, fadeMode):
		self.fadeMode = fadeMode
		self._fadeMode_callback(self.fadeMode)
		self.rccBlocks_channelModel_cc_0.set_fadeMode(self.fadeMode)

	def get_centreFreq(self):
		return self.centreFreq

	def set_centreFreq(self, centreFreq):
		self.centreFreq = centreFreq
		self.uhd_usrp_sink_0_0_0.set_center_freq(self.centreFreq, 0)

	def get_baseband_multiplier(self):
		return self.baseband_multiplier

	def set_baseband_multiplier(self, baseband_multiplier):
		self.baseband_multiplier = baseband_multiplier
		self.blocks_multiply_const_vxx_1.set_k((self.baseband_multiplier, ))

	def get_atten(self):
		return self.atten

	def set_atten(self, atten):
		self.atten = atten
		self._atten_counter.setValue(self.atten)
		self._atten_slider.setValue(self.atten)
		self.rccBlocks_VNXLabBrick_0.set_atten(self.atten)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	qapp = Qt.QApplication(sys.argv)
	tb = e100_fading_vaunix_qtgui()
	tb.start()
	tb.show()
	qapp.exec_()
	tb.stop()

