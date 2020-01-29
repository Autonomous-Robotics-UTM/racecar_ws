// All included firmware files are
// INTEL CORPORATION PROPRIETARY INFORMATION
// Copyright(c) 2019 Intel Corporation. All Rights Reserved
const int fw_D4XX_FW_Image_version[4] = {5,11,15,0};
#ifndef _MSC_VER
__asm__(
    "#version b81d8b8dcdbbf89d0b1451a3da002b255851eddc\n"
#ifdef __APPLE__
    ".const_data\n"
#define _ "_"
#else
    ".section .rodata\n"
#define _ ""
#endif
    ".global "_"fw_D4XX_FW_Image_data\n"
    _"fw_D4XX_FW_Image_data:\n"
    ".incbin \"/home/model2/racecar-ws/src/librealsense/common/fw/D4XX_FW_Image-5.11.15.0.bin\"\n"
    ".global "_"fw_D4XX_FW_Image_size\n"
    _"fw_D4XX_FW_Image_size:\n"
    "1:\n"
    ".int 1b - "_"fw_D4XX_FW_Image_data\n"
    ".previous"
);
#undef _
#endif
