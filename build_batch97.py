import json, os
from build_batch96 import _make_mufe_foundation_b96

def create_product_2207():
    return _make_mufe_foundation_b96(
        pid=2207, gtin="3548752165259",
        ar_title="كريم أساس ميك أب فور ايفر ذهبي ساند (Y373)30مل",
        en_title="MAKE UP FOR EVER Foundation Golden Sand (Y373) 30ml",
        shade_code="Y373", shade_ar="ذهبي ساند (Golden Sand)", shade_en="Golden Sand",
        tags_ar=["ميك_أب_فور_إيفر", "كريم_أساس_ميك_أب_فور_إيفر_Y373", "فاونديشن_ذهبي_ساند", "كريم_أساس_احترافي", "إكليل_أبها"],
        tags_en=["make_up_for_ever", "mufe_foundation_y373", "golden_sand_foundation", "liquid_foundation", "ekleel_abha"]
    )

def create_product_2208():
    return _make_mufe_foundation_b96(
        pid=2208, gtin="3548752165280",
        ar_title="كريم أساس ميك أب فور ايفر اللوز (Y422)30مل",
        en_title="Make Up For Ever Ultra HD Foundation - Almond (Y422) 30ml",
        shade_code="Y422", shade_ar="اللوز (Almond)", shade_en="Almond",
        tags_ar=["ميك_أب_فور_إيفر", "كريم_أساس_ميك_أب_فور_إيفر_Y422", "فاونديشن_اللوز", "كريم_أساس_احترافي", "إكليل_أبها"],
        tags_en=["make_up_for_ever", "mufe_foundation_y422", "almond_foundation", "liquid_foundation", "ekleel_abha"]
    )

def create_product_2209():
    return _make_mufe_foundation_b96(
        pid=2209, gtin="3548752165310",
        ar_title="كريم أساس ميك أب فور ايفر كونياك غامق (Y513)30مل",
        en_title="MAKE UP FOR EVER Ultra HD Foundation - Dark Cognac (Y513) 30ml",
        shade_code="Y513", shade_ar="كونياك غامق (Dark Cognac)", shade_en="Dark Cognac",
        tags_ar=["ميك_أب_فور_إيفر", "كريم_أساس_ميك_أب_فور_إيفر_Y513", "فاونديشن_كونياك_غامق", "كريم_أساس_احترافي", "إكليل_أبها"],
        tags_en=["make_up_for_ever", "mufe_foundation_y513", "dark_cognac_foundation", "liquid_foundation", "ekleel_abha"]
    )

def create_product_2210():
    return _make_mufe_foundation_b96(
        pid=2210, gtin="3548752165327",
        ar_title="كريم أساس ميك أب فور ايفر حبوب القهوه (Y522)30مل",
        en_title="MAKE UP FOR EVER Foundation - Coffee Bean (Y522) 30ml",
        shade_code="Y522", shade_ar="حبوب القهوة (Coffee Bean)", shade_en="Coffee Bean",
        tags_ar=["ميك_أب_فور_إيفر", "كريم_أساس_ميك_أب_فور_إيفر_Y522", "فاونديشن_حبوب_القهوة", "كريم_أساس_احترافي", "إكليل_أبها"],
        tags_en=["make_up_for_ever", "mufe_foundation_y522", "coffee_bean_foundation", "liquid_foundation", "ekleel_abha"]
    )

def create_product_2211():
    return _make_mufe_foundation_b96(
        pid=2211, gtin="3548752165334",
        ar_title="كريم أساس ميك أب فور ايفر بني (Y532)30مل",
        en_title="Make Up For Ever Foundation Brown (Y532) 30ml",
        shade_code="Y532", shade_ar="بني (Brown)", shade_en="Brown",
        tags_ar=["ميك_أب_فور_إيفر", "كريم_أساس_ميك_أب_فور_إيفر_Y532", "فاونديشن_بني", "كريم_أساس_احترافي", "إكليل_أبها"],
        tags_en=["make_up_for_ever", "mufe_foundation_y532", "brown_foundation", "liquid_foundation", "ekleel_abha"]
    )

print("Loaded all 5 Batch 97 builders complete")
