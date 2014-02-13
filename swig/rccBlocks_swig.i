/* -*- c++ -*- */

#define RCCBLOCKS_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "rccBlocks_swig_doc.i"

%{
#include "rccBlocks/channelModel_cc.h"
%}


%include "rccBlocks/channelModel_cc.h"
GR_SWIG_BLOCK_MAGIC2(rccBlocks, channelModel_cc);
