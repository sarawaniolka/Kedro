# Creates an http request to a webserver
# Using webhook.site

#curl {link}
# adding data
# curl --data hello=world {link}

from kedro.pipeline.node import Node
from kedro.framework.hooks import hook_impl
import requests

class WebAPICallingHook:
    url = "https://webhook.site/78accda2-6e96-485a-8f7f-2df06c02af47"
    @hook_impl
    def after_node_run(node: Node, catalog, inputs, outputs, is_async): #name from the function from docs
        success = False
        while not success:
            resp = requests.post(WebAPICallingHook.url, {
                'hook': 'before_node_run', 
                'node': 'add_data',
            })
            success = resp.status_code == 200 #determing if it was a success
    
    @hook_impl        
    def before_node_run(node: Node, catalog, inputs): #arguments from doc
        success = False
        while not success:
            resp = requests.post(WebAPICallingHook.url, {
                'hook': 'after_node_run', 
                'node': 'add_data',
            })
            success = resp.status_code == 200 #determing if it was a success