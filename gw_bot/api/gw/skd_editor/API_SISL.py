import json

from pbx_gs_python_utils.utils.Files import Files


class API_SISL:
    def __init__(self):
        self.tag_names   = ['FileStream','DOCUMENT','STRUCTARRAY', 'VALUEARRAY',
                            'STRUCT','VALUE',
                            'ITEM']
        self.field_names = ['cameraname','streamname', '__children',
                            'name', 'estrc','offset','size', 'eitem',
                            '__data']

    def convert_sisl_file_to_json(self, path_to_file):
        sisl_data = Files.contents(path_to_file)
        return self.convert_sisl_to_json(sisl_data)

    def convert_sisl_to_json(self, sisl_data):
        mappings = [  ('__struct'      , '"__struct'     ),
                      ('__meta: !__'   , '"meta":'       )]

        for tag_name in self.tag_names:
            mappings.append((f'!{tag_name}', f'{tag_name}":'))

        for field_name in self.field_names:
            mappings.append((f'{field_name}: !__', f'"{field_name}":'))

        # json_data = ""
        # for line in sisl_data.splitlines():
        #     for key, value in mappings:
        #         line = line.replace(key,value)
        #     json_data += f'{line}\n'
        json_data = sisl_data
        for key, value in mappings:
            json_data = json_data.replace(key,value)
        return json.loads(json_data)

    def convert_json_to_sisl(self, json_data):

        mappings = [('"__struct', '__struct'    ),
            ('"meta":'  , '__meta: !__' )]

        for tag_name in self.tag_names:
            mappings.append((f'{tag_name}":', f'!{tag_name}'))

        for field_name in self.field_names:
            mappings.append((f'"{field_name}":', f'{field_name}: !__'))

        #sisl_data = ""
        #for line in json.dumps(json_data,indent=2).splitlines():
        #    for key, value in mappings:
        #        line = line.replace(key, value)
        #    sisl_data += f'{line}\n'

        sisl_data = json.dumps(json_data,indent=2)
        for key, value in mappings:
            sisl_data = sisl_data.replace(key, value)
        #    sisl_data += f'{line}\n'
        return sisl_data

    def convert_json_to_sisl_file(self, json_data, sisl_file):
        sisl_data = self.convert_json_to_sisl(json_data)
        Files.write(sisl_file, sisl_data)
        return sisl_file