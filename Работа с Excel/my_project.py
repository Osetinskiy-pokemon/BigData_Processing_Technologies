import xlwings as xw
# @xw.func is a decorator. 
# It must be added right before the def to let xlwings know this is a user-defined function.
#@xw.func
#def validate(sheet,reviews_sample):
recipes_sample_with_tags_ingredients_new =  recipes_sample_with_tags_ingredients_new["id"].tolist()
for i in range(2,len(reviews_sample.shape[0])):
    if (int(sheet.range((i,6)).value) >=0) and ((int(sheet.range((i,6)).value) <=5) and ((int(sheet.range((i,2)).value) in recipes_sample_with_tags_ingredients_new):                                
        pass
    else:
        for j in range(1,9):
            sheet.range((i,j)).color = (220, 20, 60)
