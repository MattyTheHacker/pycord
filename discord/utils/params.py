def filter_params(params, **kwargs):
    for old_param, new_param in kwargs.items():
        if old_param in params:
            if new_param is None:
                params.pop(old_param)
            else:
                params[new_param] = params.pop(old_param)
    return params
