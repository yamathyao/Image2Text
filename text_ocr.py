import os

from aip import AipOcr

# 认证信息
APP_ID = "1700000"
API_KEY = "F000000000000000000000"
SECRET_KEY = "k0000000000000000000000000000000000000"


def get_ocr_str(file_path, general_or_accurate, origin_format=True):
    """
    图片转文字
    :param: file_path 图片路径
    :return:
    """
    with open(file_path, 'rb') as fp:
        file_bytes = fp.read()
    return get_ocr_str_from_bytes(file_bytes, general_or_accurate, origin_format)


def get_ocr_str_from_bytes(file_bytes, general_or_accurate, origin_format=True):
    """
    图片转文字
    :param file_bytes: 图片的字节
    :param general_or_accurate
    :param origin_format:
    :return:
    """
    options_general = {
        'detect_direction': 'false',
        'language_type': 'CHN_ENG',
    }

    options_accurate = {
        'detect_direction': 'false',
        'probability': 'false'
    }

    ocr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    if general_or_accurate == 'general':
        result_dict = ocr.basicGeneral(file_bytes, options_general)
    else:
        result_dict = ocr.basicAccurate(file_bytes, options_accurate)
    if origin_format:
        result_str = '\n'.join([entity['words'] for entity in result_dict['words_result']])
    else:
        result_str = ''.join([entity['words'] for entity in result_dict['words_result']])
    return result_str


if __name__ == '__main__':
    IMAGE_PATH = "C://Users//GEEX177//Desktop//test.jpg"
    print(get_ocr_str(IMAGE_PATH, 'accurate'))
