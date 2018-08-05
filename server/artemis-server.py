import random
from flask import Flask, jsonify
from flasgger import APISpec, Schema, Swagger, fields



app = Flask(__name__)





@app.route('/random')
def random_pet():
    """
    A cute furry animal endpoint.
    Get a random pet
    ---
    description: Get a random pet
    responses:
        200:
            description: A pet to be returned
            schema:
                $ref: '#/definitions/Pet'
    """
    pet = {'category': [{'id': 1, 'name': 'rodent'}], 'name': 'Mickey'}
    return jsonify(PetSchema().dump(pet).data)



"""
optionally if using apispec.APISpec from original module
you can do:

from flasgger.utils import apispec_to_template
template = apispec_to_template(
    app=app,
    spec=spec,
    definitions=[CategorySchema, PetSchema],
    paths=[random_pet]
)

"""

# start Flasgger using a template from apispec
swag = Swagger(app)


if __name__ == '__main__':
    app.run(debug=True)