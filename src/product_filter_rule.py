def is_need(product, settings):
    return product.is_adult == False \
        and product.author not in settings.author_black_list
