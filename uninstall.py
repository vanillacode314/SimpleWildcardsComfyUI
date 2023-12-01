try:
    import os, shutil
    import folder_paths

    module_js_directory = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "js"
    )
    application_root_directory = os.path.dirname(folder_paths.__file__)
    application_web_extensions_directory = os.path.join(
        application_root_directory, "web", "extensions", "vanilla.simple.wildcard"
    )
    shutil.rmtree(application_web_extensions_directory)
except:
    pass
