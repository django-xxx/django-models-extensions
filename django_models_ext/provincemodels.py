# -*- coding: utf-8 -*-

from django.db import models
from django_six import gettext_lazy as _


class ProvinceModelMixin(models.Model):
    PROVINCE_CODE_NAME_DICT = {
        "110000": u"北京市",
        "120000": u"天津市",
        "130000": u"河北省",
        "140000": u"山西省",
        "150000": u"内蒙古自治区",
        "210000": u"辽宁省",
        "220000": u"吉林省",
        "230000": u"黑龙江省",
        "310000": u"上海市",
        "320000": u"江苏省",
        "330000": u"浙江省",
        "340000": u"安徽省",
        "350000": u"福建省",
        "360000": u"江西省",
        "370000": u"山东省",
        "410000": u"河南省",
        "420000": u"湖北省",
        "430000": u"湖南省",
        "440000": u"广东省",
        "450000": u"广西壮族自治区",
        "460000": u"海南省",
        "500000": u"重庆市",
        "510000": u"四川省",
        "520000": u"贵州省",
        "530000": u"云南省",
        "540000": u"西藏自治区",
        "610000": u"陕西省",
        "620000": u"甘肃省",
        "630000": u"青海省",
        "640000": u"宁夏回族自治区",
        "650000": u"新疆维吾尔自治区",
        "710000": u"台湾省",
        "810000": u"香港特别行政区",
        "820000": u"澳门特别行政区"
    }

    # dict((v, k) for k, v in PROVINCE_CODE.iteritems())
    PROVINCE_NAME_CODE_DICT = {
        u"北京市": "110000",
        u"天津市": "120000",
        u"河北省": "130000",
        u"山西省": "140000",
        u"内蒙古自治区": "150000",
        u"辽宁省": "210000",
        u"吉林省": "220000",
        u"黑龙江省": "230000",
        u"上海市": "310000",
        u"江苏省": "320000",
        u"浙江省": "330000",
        u"安徽省": "340000",
        u"福建省": "350000",
        u"江西省": "360000",
        u"山东省": "370000",
        u"河南省": "410000",
        u"湖北省": "420000",
        u"湖南省": "430000",
        u"广东省": "440000",
        u"广西壮族自治区": "450000",
        u"海南省": "460000",
        u"重庆市": "500000",
        u"四川省": "510000",
        u"贵州省": "520000",
        u"云南省": "530000",
        u"西藏自治区": "540000",
        u"陕西省": "610000",
        u"甘肃省": "620000",
        u"青海省": "630000",
        u"宁夏回族自治区": "640000",
        u"新疆维吾尔自治区": "650000",
        u"台湾省": "710000",
        u"香港特别行政区": "810000",
        u"澳门特别行政区": "820000"
    }

    # tuple((k, k) for k, v in PROVINCE_CODE.iteritems())
    PROVINCE_CODE_TUPLE = (
        ("110000", "110000"),
        ("120000", "120000"),
        ("130000", "130000"),
        ("140000", "140000"),
        ("150000", "150000"),
        ("210000", "210000"),
        ("220000", "220000"),
        ("230000", "230000"),
        ("310000", "310000"),
        ("320000", "320000"),
        ("330000", "330000"),
        ("340000", "340000"),
        ("350000", "350000"),
        ("360000", "360000"),
        ("370000", "370000"),
        ("410000", "410000"),
        ("420000", "420000"),
        ("430000", "430000"),
        ("440000", "440000"),
        ("450000", "450000"),
        ("460000", "460000"),
        ("500000", "500000"),
        ("510000", "510000"),
        ("520000", "520000"),
        ("530000", "530000"),
        ("540000", "540000"),
        ("610000", "610000"),
        ("620000", "620000"),
        ("630000", "630000"),
        ("640000", "640000"),
        ("650000", "650000"),
        ("710000", "710000"),
        ("810000", "810000"),
        ("820000", "820000")
    )

    # tuple((v, v) for k, v in PROVINCE_CODE.iteritems())
    PROVINCE_NAME_TUPLE = (
        (u"北京市", u"北京市"),
        (u"天津市", u"天津市"),
        (u"河北省", u"河北省"),
        (u"山西省", u"山西省"),
        (u"内蒙古自治区", u"内蒙古自治区"),
        (u"辽宁省", u"辽宁省"),
        (u"吉林省", u"吉林省"),
        (u"黑龙江省", u"黑龙江省"),
        (u"上海市", u"上海市"),
        (u"江苏省", u"江苏省"),
        (u"浙江省", u"浙江省"),
        (u"安徽省", u"安徽省"),
        (u"福建省", u"福建省"),
        (u"江西省", u"江西省"),
        (u"山东省", u"山东省"),
        (u"河南省", u"河南省"),
        (u"湖北省", u"湖北省"),
        (u"湖南省", u"湖南省"),
        (u"广东省", u"广东省"),
        (u"广西壮族自治区", u"广西壮族自治区"),
        (u"海南省", u"海南省"),
        (u"重庆市", u"重庆市"),
        (u"四川省", u"四川省"),
        (u"贵州省", u"贵州省"),
        (u"云南省", u"云南省"),
        (u"西藏自治区", u"西藏自治区"),
        (u"陕西省", u"陕西省"),
        (u"甘肃省", u"甘肃省"),
        (u"青海省", u"青海省"),
        (u"宁夏回族自治区", u"宁夏回族自治区"),
        (u"新疆维吾尔自治区", u"新疆维吾尔自治区"),
        (u"台湾省", u"台湾省"),
        (u"香港特别行政区", u"香港特别行政区"),
        (u"澳门特别行政区", u"澳门特别行政区")
    )

    PROVINCE_DEFAULT_CODE = '110000'
    PROVINCE_DEFAULT_NAME = u'北京市'

    province_code = models.CharField(_(u'province_code'), max_length=6, choices=PROVINCE_CODE_TUPLE, default=PROVINCE_DEFAULT_CODE, help_text=_(u'province_code'), db_index=True)
    province_name = models.CharField(_(u'province_name'), max_length=10, choices=PROVINCE_NAME_TUPLE, default=PROVINCE_DEFAULT_NAME, help_text=_(u'province_name'), db_index=True)

    class Meta:
        abstract = True


class ProvinceShortModelMixin(models.Model):
    PROVINCE_CODE_NAME_DICT = {
        "110000": u"北京",
        "120000": u"天津",
        "130000": u"河北",
        "140000": u"山西",
        "150000": u"内蒙古",
        "210000": u"辽宁",
        "220000": u"吉林",
        "230000": u"黑龙江",
        "310000": u"上海",
        "320000": u"江苏",
        "330000": u"浙江",
        "340000": u"安徽",
        "350000": u"福建",
        "360000": u"江西",
        "370000": u"山东",
        "410000": u"河南",
        "420000": u"湖北",
        "430000": u"湖南",
        "440000": u"广东",
        "450000": u"广西",
        "460000": u"海南",
        "500000": u"重庆",
        "510000": u"四川",
        "520000": u"贵州",
        "530000": u"云南",
        "540000": u"西藏",
        "610000": u"陕西",
        "620000": u"甘肃",
        "630000": u"青海",
        "640000": u"宁夏",
        "650000": u"新疆",
        "710000": u"台湾",
        "810000": u"香港",
        "820000": u"澳门"
    }

    # dict((v, k) for k, v in PROVINCE_CODE.iteritems())
    PROVINCE_NAME_CODE_DICT = {
        u"北京": "110000",
        u"天津": "120000",
        u"河北": "130000",
        u"山西": "140000",
        u"内蒙古": "150000",
        u"辽宁": "210000",
        u"吉林": "220000",
        u"黑龙江": "230000",
        u"上海": "310000",
        u"江苏": "320000",
        u"浙江": "330000",
        u"安徽": "340000",
        u"福建": "350000",
        u"江西": "360000",
        u"山东": "370000",
        u"河南": "410000",
        u"湖北": "420000",
        u"湖南": "430000",
        u"广东": "440000",
        u"广西": "450000",
        u"海南": "460000",
        u"重庆": "500000",
        u"四川": "510000",
        u"贵州": "520000",
        u"云南": "530000",
        u"西藏": "540000",
        u"陕西": "610000",
        u"甘肃": "620000",
        u"青海": "630000",
        u"宁夏": "640000",
        u"新疆": "650000",
        u"台湾": "710000",
        u"香港": "810000",
        u"澳门": "820000"
    }

    # tuple((k, k) for k, v in PROVINCE_CODE.iteritems())
    PROVINCE_CODE_TUPLE = (
        ("110000", "110000"),
        ("120000", "120000"),
        ("130000", "130000"),
        ("140000", "140000"),
        ("150000", "150000"),
        ("210000", "210000"),
        ("220000", "220000"),
        ("230000", "230000"),
        ("310000", "310000"),
        ("320000", "320000"),
        ("330000", "330000"),
        ("340000", "340000"),
        ("350000", "350000"),
        ("360000", "360000"),
        ("370000", "370000"),
        ("410000", "410000"),
        ("420000", "420000"),
        ("430000", "430000"),
        ("440000", "440000"),
        ("450000", "450000"),
        ("460000", "460000"),
        ("500000", "500000"),
        ("510000", "510000"),
        ("520000", "520000"),
        ("530000", "530000"),
        ("540000", "540000"),
        ("610000", "610000"),
        ("620000", "620000"),
        ("630000", "630000"),
        ("640000", "640000"),
        ("650000", "650000"),
        ("710000", "710000"),
        ("810000", "810000"),
        ("820000", "820000")
    )

    # tuple((v, v) for k, v in PROVINCE_CODE.iteritems())
    PROVINCE_NAME_TUPLE = (
        (u"北京", u"北京"),
        (u"天津", u"天津"),
        (u"河北", u"河北"),
        (u"山西", u"山西"),
        (u"内蒙古", u"内蒙古"),
        (u"辽宁", u"辽宁"),
        (u"吉林", u"吉林"),
        (u"黑龙江", u"黑龙江"),
        (u"上海", u"上海"),
        (u"江苏", u"江苏"),
        (u"浙江", u"浙江"),
        (u"安徽", u"安徽"),
        (u"福建", u"福建"),
        (u"江西", u"江西"),
        (u"山东", u"山东"),
        (u"河南", u"河南"),
        (u"湖北", u"湖北"),
        (u"湖南", u"湖南"),
        (u"广东", u"广东"),
        (u"广西", u"广西"),
        (u"海南", u"海南"),
        (u"重庆", u"重庆"),
        (u"四川", u"四川"),
        (u"贵州", u"贵州"),
        (u"云南", u"云南"),
        (u"西藏", u"西藏"),
        (u"陕西", u"陕西"),
        (u"甘肃", u"甘肃"),
        (u"青海", u"青海"),
        (u"宁夏", u"宁夏"),
        (u"新疆", u"新疆"),
        (u"台湾", u"台湾"),
        (u"香港", u"香港"),
        (u"澳门", u"澳门")
    )

    PROVINCE_DEFAULT_CODE = '110000'
    PROVINCE_DEFAULT_NAME = u'北京'

    province_code = models.CharField(_(u'province_code'), max_length=6, choices=PROVINCE_CODE_TUPLE, default=PROVINCE_DEFAULT_CODE, help_text=_(u'province_code'), db_index=True)
    province_name = models.CharField(_(u'province_name'), max_length=3, choices=PROVINCE_NAME_TUPLE, default=PROVINCE_DEFAULT_NAME, help_text=_(u'province_name'), db_index=True)

    class Meta:
        abstract = True
