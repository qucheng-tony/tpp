from flask_restful import Resource, fields, marshal

from App.apis.api_constant import HTTP_OK
from App.models.common import City, Letter
city_filds={
    'id':fields.Integer(attribute='c_id'),
    'parentId':fields.Integer(attribute='c_parent_id'),
    'redionName':fields.String(attribute='c_redion_name'),
    'cityCode':fields.String(attribute='c_city_code'),
    'pinYin':fields.String(attribute='c_pinyin'),
}

class CitiesResource(Resource):
    def get(self):
        letters=Letter.query.all()
        letters_citys={}
        letters_citys_filds={}
        for letter in letters:
            letter_cities=City.query.filter_by(letter_id=letter.id)
            letters_citys[letter.letter]=letter_cities
            letters_citys_filds[letter.letter]=fields.List(fields.Nested(city_filds))
        data={
            'msg':'ok',
            'status':HTTP_OK,
            'data':marshal(letters_citys,letters_citys_filds)
        }

        return data