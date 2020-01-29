#pragma once

#define FW_CENTRAL_BL_VERSION "1.0.1.112"

extern "C" const unsigned char fw_central_bl_data[];
extern "C" const int           fw_central_bl_size;
extern "C" const int           fw_central_bl_version[4];

#ifdef _MSC_VER
#include <windows.h>
extern "C" IMAGE_DOS_HEADER __ImageBase;
#endif

static inline const unsigned char *fw_get_central_bl(int &size)
{
#ifdef _MSC_VER
    HRSRC rc = ::FindResourceA((HMODULE)&__ImageBase, "CENTRAL_BL_DATA" , "CENTRAL_BL_RC");
    HGLOBAL data = ::LoadResource((HMODULE)&__ImageBase, rc);
    size = ::SizeofResource((HMODULE)&__ImageBase, rc);
    return static_cast<const unsigned char*>(::LockResource(data));
#else
    size = fw_central_bl_size;
    return fw_central_bl_data;
#endif
}
