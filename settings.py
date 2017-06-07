import os
base_dir = os.path.dirname(__file__)

settings = dict(
    template_path=os.path.join(base_dir, "templates"),
    static_path=os.path.join(base_dir, "static"),
    debug=True,
    title="abcde",
)
