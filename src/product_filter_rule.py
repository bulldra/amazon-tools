def is_need(product, settings):
    return product.is_adult == False \
        and len(set(product.genles) & set(settings.genle_balck_list)) == 0 \
        and len(set(product.authors) & set(settings.author_black_list)) == 0
