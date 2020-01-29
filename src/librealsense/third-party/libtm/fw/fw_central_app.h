#pragma once

#define FW_CENTRAL_APP_VERSION "2.0.19.271"

extern "C" const unsigned char fw_central_app_data[];
extern "C" const int           fw_central_app_size;
extern "C" const int           fw_central_app_version[4];

#ifdef _MSC_VER
#include <windows.h>
extern "C" IMAGE_DOS_HEADER __ImageBase;
#endif

static inline const unsigned char *fw_get_central_app(int &size)
{
#ifdef _MSC_VER
    HRSRC rc = ::FindResourceA((HMODULE)&__ImageBase, "CENTRAL_APP_DATA" , "CENTRAL_APP_RC");
    HGLOBAL data = ::LoadResource((HMODULE)&__ImageBase, rc);
    size = ::SizeofResource((HMODULE)&__ImageBase, rc);
    return static_cast<const unsigned char*>(::LockResource(data));
#else
    size = fw_central_app_size;
    return fw_central_app_data;
#endif
}
