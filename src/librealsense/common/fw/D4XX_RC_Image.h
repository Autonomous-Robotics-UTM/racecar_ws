#pragma once

#define FW_D4XX_RC_IMAGE_VERSION "5.11.15.0"

extern "C" const unsigned char fw_D4XX_RC_Image_data[];
extern "C" const int           fw_D4XX_RC_Image_size;
extern "C" const int           fw_D4XX_RC_Image_version[4];

#ifdef _MSC_VER
#include <windows.h>
extern "C" IMAGE_DOS_HEADER __ImageBase;
#endif

static inline const unsigned char *fw_get_D4XX_RC_Image(int &size)
{
#ifdef _MSC_VER
    HRSRC rc = ::FindResourceA((HMODULE)&__ImageBase, "D4XX_RC_IMAGE_DATA" , "D4XX_RC_IMAGE_RC");
    HGLOBAL data = ::LoadResource((HMODULE)&__ImageBase, rc);
    size = ::SizeofResource((HMODULE)&__ImageBase, rc);
    return static_cast<const unsigned char*>(::LockResource(data));
#else
    size = fw_D4XX_RC_Image_size;
    return fw_D4XX_RC_Image_data;
#endif
}
