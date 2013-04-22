/* -*- c++ -*- */
/* 
 * Copyright 2013 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */


#ifndef INCLUDED_RCCBLOCKS_SQUARE2_FF_H
#define INCLUDED_RCCBLOCKS_SQUARE2_FF_H

#include <rccBlocks/api.h>
#include <gr_sync_block.h>

namespace gr {
  namespace rccBlocks {

    /*!
     * \brief <+description of block+>
     * \ingroup rccBlocks
     *
     */
    class RCCBLOCKS_API square2_ff : virtual public gr_sync_block
    {
     public:
      typedef boost::shared_ptr<square2_ff> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of rccBlocks::square2_ff.
       *
       * To avoid accidental use of raw pointers, rccBlocks::square2_ff's
       * constructor is in a private implementation
       * class. rccBlocks::square2_ff::make is the public interface for
       * creating new instances.
       */
      static sptr make();
    };

  } // namespace rccBlocks
} // namespace gr

#endif /* INCLUDED_RCCBLOCKS_SQUARE2_FF_H */

