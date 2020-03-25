import json

import pymysql


def load():
    with open('code/data/cities.json') as city_file:
        file_str=city_file.read()
    return json.loads(file_str)

def insert_city(city_json):
    citys_file=city_json.get("returnValue")
    print(citys_file)
    letter=citys_file.keys()
    db = pymysql.Connect(host='localhost', port=3306, user='root', password='0118', database="flaskTpp",
                         charset='utf8')

    cursor = db.cursor()

    for key in letter:
        # print(key)

        cursor.execute("INSERT INTO letter(letter) VALUES ('%s');" % key)

        db.commit()

        cursor.execute("SELECT letter.id FROM letter WHERE letter='%s'" % key)

        letter_id = cursor.fetchone()[0]

        print(letter_id)

        cities_letter = citys_file.get(key)

        for city in cities_letter:
            print(city)

            c_id = city.get('id')
            c_parent_id = city.get('parentId')
            c_region_name = city.get('regionName')
            c_city_code = city.get('cityCode')
            c_pinyin = city.get('pinYin')

            cursor.execute(
                "INSERT INTO city(letter_id, c_id, c_parent_id, c_region_name, c_city_code, c_pinyin) VALUES (%d, %d, %d, '%s', %d, '%s');" % (
                letter_id, c_id, c_parent_id, c_region_name, c_city_code, c_pinyin))

            db.commit()


if __name__=="__main__":
    city_json=load()

    insert_city(city_json)