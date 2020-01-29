// All included firmware files are
// INTEL CORPORATION PROPRIETARY INFORMATION
// Copyright(c) 2019 Intel Corporation. All Rights Reserved
const int fw_target_version[4] = {0,1,0,279};
#ifndef _MSC_VER
__asm__(
    "#version 3b30f13e04a932a261d7d5f59a9b7ca0fd342758\n"
#ifdef __APPLE__
    ".const_data\n"
#define _ "_"
#else
    ".section .rodata\n"
#define _ ""
#endif
    ".global "_"fw_target_data\n"
    _"fw_target_data:\n"
    ".incbin \"/home/model2/racecar-ws/src/librealsense/third-party/libtm/fw/target-0.1.0.279.mvcmd\"\n"
    ".global "_"fw_target_size\n"
    _"fw_target_size:\n"
    "1:\n"
    ".int 1b - "_"fw_target_data\n"
    ".previous"
);
#undef _
#endif
