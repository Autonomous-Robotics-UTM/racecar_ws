// All included firmware files are
// INTEL CORPORATION PROPRIETARY INFORMATION
// Copyright(c) 2019 Intel Corporation. All Rights Reserved
const int fw_central_app_version[4] = {2,0,19,271};
#ifndef _MSC_VER
__asm__(
    "#version cab0011e9e18edc8bcca20afb2f944399ac8b81c\n"
#ifdef __APPLE__
    ".const_data\n"
#define _ "_"
#else
    ".section .rodata\n"
#define _ ""
#endif
    ".global "_"fw_central_app_data\n"
    _"fw_central_app_data:\n"
    ".incbin \"/home/model2/racecar-ws/src/librealsense/third-party/libtm/fw/central_app-2.0.19.271.bin\"\n"
    ".global "_"fw_central_app_size\n"
    _"fw_central_app_size:\n"
    "1:\n"
    ".int 1b - "_"fw_central_app_data\n"
    ".previous"
);
#undef _
#endif
