// All included firmware files are
// INTEL CORPORATION PROPRIETARY INFORMATION
// Copyright(c) 2019 Intel Corporation. All Rights Reserved
const int fw_central_bl_version[4] = {1,0,1,112};
#ifndef _MSC_VER
__asm__(
    "#version d8fb5ba6f7029a3c950bf6b1ef5715efd880ef66\n"
#ifdef __APPLE__
    ".const_data\n"
#define _ "_"
#else
    ".section .rodata\n"
#define _ ""
#endif
    ".global "_"fw_central_bl_data\n"
    _"fw_central_bl_data:\n"
    ".incbin \"/home/model2/racecar-ws/src/librealsense/third-party/libtm/fw/central_bl-1.0.1.112.bin\"\n"
    ".global "_"fw_central_bl_size\n"
    _"fw_central_bl_size:\n"
    "1:\n"
    ".int 1b - "_"fw_central_bl_data\n"
    ".previous"
);
#undef _
#endif
