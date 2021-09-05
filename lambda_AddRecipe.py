import boto3
import json

my_bucket = 'lazydinners'
my_key = 'allrecipes.json'


def Create_Recipe():

    """Pull Recipes from current list"""
    s3 = boto3.client('s3')

    object = s3.get_object(Bucket = my_bucket, Key = my_key)
    object_data = json.loads(object['Body'].read())
        
    data = []
    data += object_data
    
    recipes = data
    
    """Adds a recipe to the list"""
	#Example
	#curl -H "Content-Type: application/json" -X POST -d '{"name":"recipename","ingredients":"ingredient1, ingredient2, ingredient3","side_ideas":"idea1, idea2, idea3","difficulty":"difficultylevel"}' http://localhost:5000/recipe/api/v1.0/newrecipe
    if not request.json or not "name" in request.json or not "ingredients" in request.json or not "side_ideas" in request.json or not "difficulty" in request.json:
        abort(400)
    recipe = {
        "name": request.json.get("name", ""),
        "ingredients": request.json.get("ingredients", ""),
	"side_ideas": request.json.get("side_ideas", ""),
	"difficulty": request.json.get("difficulty", "")
    }
    recipes.append(recipe)

    newrecipes = json.dumps(recipes)

    try:
    	s3.put_object(Body = newrecipes, Bucket = my_bucket, Key = my_key)
	return jsonify({'Succesffuly added the recipe ': recipe["name"]})
    except:
	return jsonify({'You messed up the s3 put call.'})
	
def lambda_handler(event, context):
    # Call the Create_Recipe function and return appropriately formatted results.
    return {'isBase64Encoded': False,'statusCode': 200,'body': json.dumps(Create_Recipe()), 'headers': {"Access-Control-Allow-Origin": "*"}}
