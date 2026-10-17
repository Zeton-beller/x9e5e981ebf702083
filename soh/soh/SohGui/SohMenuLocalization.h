#ifndef SOH_MENU_LOCALIZATION_H
#define SOH_MENU_LOCALIZATION_H

#include <string>
#include <unordered_map>
#include "soh/SohGui/MenuTypes.h"

namespace SohGui {
    void ApplySohMenuLocalization(std::unordered_map<std::string, MainMenuEntry>& menuEntries);
    std::string TranslateSidebar(const std::string& sidebar);
    std::string TranslateHeader(const std::string& header);
    const char* TranslateComboOption(const char* option);
}

#endif // SOH_MENU_LOCALIZATION_H
