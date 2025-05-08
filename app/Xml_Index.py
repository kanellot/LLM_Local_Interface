class XMLIndexConstants:
    # --- Etiquetas del XML de configuración de la app ---
    app_conf_keys = {
        "LANGUAGE": "language",
        "PROMPT_CONFIG_PATH": "prompt_config_path",
        "APP_MESSAGES_PATH": "app_messages_path"
    }

    model_conf_keys = {
        "MODEL_PATH": "model_path",
        "CONSOLE_DBG": "console_dbg",
        "ENABLE_MODEL": "enable_model",
        "MAX_TOKENS": "max_tokens",
        "MAX_FILE_CHARS": "max_file_chars",
        "USE_CUDA": "use_cuda",
        "N_GPU_LAYERS": "n_gpu_layers",
    }

    prompt_conf_keys = {
        "RULES": "rules",
        "PRE_PROMPT": "pre_prompt",
        "LEER_PRE_PROMPT": "leer_pre_prompt",
        "LEER_POST_PROMPT": "leer_post_prompt"
    }

    app_info_conf_keys = {
        "APP_START": "app_start",
        "CONFIG_LOAD_PASS": "config_pass",
        "CONFIG_LOAD_LANG_PASS": "config_lang_pass"
    }

    app_error_conf_keys = {
        "CONFIG_NAME_ERROR": "config_error",
        "CONFIG_LOAD_ERROR": "config_load",
        "CONFIG_LOAD_LANG_ERROR": "config_lang_error",
        "MODEL_LOAD_ERROR": "model_load_error",
        "FILE_LOAD_ERROR": "file_load_error",
        "EMPTY_FOLDER_ERROR": "empty_folder_error",
    }

