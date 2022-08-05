from evomol import run_model

model_path = "examples/test_millad_3"

run_model({
    "obj_function": "antiH",
    "optimization_parameters": {
        "max_steps": 50,
        "pop_max_size": 10,
        "k_to_replace": 2,
        "mutable_init_pop": False
    },
    "io_parameters": {
        "model_path": model_path,
        "record_history": True,
        "smiles_list_init_path": "examples/best.smi"
    }
})
