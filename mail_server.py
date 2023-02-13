from typing import Dict, List, Optional
from flask import Flask, request, jsonify
import pathlib
import uuid
import json


app = Flask(__name__)
thisdir = pathlib.Path(__file__).parent.absolute() # path to directory of this file

# Function to load and save the mail to/from the json file

def load_mail() -> List[Dict[str, str]]:
    """
    Loads the mail from the json file

    Returns:
        list: A list of dictionaries representing the mail entries
    """
    try:
        return json.loads(thisdir.joinpath('mail_db.json').read_text())
    except FileNotFoundError:
        return []

def save_mail(mail: List[Dict[str, str]]) -> None:
    """TODO: fill out this docstring (using the load_mail docstring as a guide)
    
    Writes the mail list of dictionaries to the json file to save it

    Args:
        List: list of dictionaries representing the mail entries

    Returns:
        None
    """
    thisdir.joinpath('mail_db.json').write_text(json.dumps(mail, indent=4))

def add_mail(mail_entry: Dict[str, str]) -> str:
    """TODO: fill out this docstring (using the load_mail docstring as a guide)

    Appends the input mail entry onto the list of entries

    Args:
        Dict: mail entry to be appended onto the list of entries
    
    Returns:
        str: unique id of the new mail entry
    
    """
    mail = load_mail()
    mail.append(mail_entry)
    mail_entry['id'] = str(uuid.uuid4()) # generate a unique id for the mail entry
    save_mail(mail)
    return mail_entry['id']

def delete_mail(mail_id: str) -> bool:
    """TODO: fill out this docstring (using the load_mail docstring as a guide)

    Searches the mail list. If an id on the entry list matches the input id, the pop function is called to delete it.

    Args:
        str: id of the mail entry to be deleted

    Returns:
        bool: True is the mail is found and deleted, False if the mail id is not found
    """
    mail = load_mail()
    for i, entry in enumerate(mail):
        if entry['id'] == mail_id:
            mail.pop(i)
            save_mail(mail)
            return True

    return False

def get_mail(mail_id: str) -> Optional[Dict[str, str]]:
    """TODO: fill out this docstring (using the load_mail docstring as a guide)
    
    Fetches the mail entry corresponding to the mail id that the user input

    Args:
        str: id of the desired mail entry

    Returns:
        Dict: If the id is found, the corresponding mail entry is returned
        If the id is not found, nothing is returned

    """
    mail = load_mail()
    for entry in mail:
        if entry['id'] == mail_id:
            return entry

    return None

def get_inbox(recipient: str) -> List[Dict[str, str]]:
    """TODO: fill out this docstring (using the load_mail docstring as a guide)

    Searches mail and creates a list of all the entries for the specified recipient

    Args:
        str: recipient name of the user whose inbox we want to see

    Returns:
        List: list of mail entry dictionaries for the recipient

    """
    mail = load_mail()
    inbox = []
    for entry in mail:
        if entry['recipient'] == recipient:
            inbox.append(entry)

    return inbox

def get_sent(sender: str) -> List[Dict[str, str]]:
    """TODO: fill out this docstring (using the load_mail docstring as a guide)

    Searches mail and creates a list of all the entries that have been sent by the specified user

    Args:
        str: name of the sender

    Returns:
        List: list of mail entry dictionaries sent by the specified user

    """
    mail = load_mail()
    sent = []
    for entry in mail:
        if entry['sender'] == sender:
            sent.append(entry)

    return sent

# API routes - these are the endpoints that the client can use to interact with the server
@app.route('/mail', methods=['POST'])
def add_mail_route():
    """
    Summary: Adds a new mail entry to the json file and sends the client the id of the new entry

    Returns:
        jsonified dictionary with key "id" and value: id of the mail entry
    """
    mail_entry = request.get_json()
    mail_id = add_mail(mail_entry)
    res = jsonify({'id': mail_id})
    res.status_code = 201 # Status code for "created"
    return res

@app.route('/mail/<mail_id>', methods=['DELETE'])
def delete_mail_route(mail_id: str):
    """
    Summary: Deletes a mail entry from the json file and sends the client a confirmation

    Args:
        mail_id (str): The id of the mail entry to delete

    Returns:
        jsonified dictionary with key "deleted" and value: True or False
        True if the mail was found and deleted properly
        False otherwise
    """
    # TODO: implement this function
    res = jsonify({'deleted': delete_mail(mail_id)})
    res.status_code = 200
    return res

@app.route('/mail/<mail_id>', methods=['GET'])
def get_mail_route(mail_id: str):
    """
    Summary: Gets a mail entry from the json file and sends it to the client

    Args:
        mail_id (str): The id of the mail entry to get

    Returns:
        A jsonified dictionary representing the mail entry if it exists, None otherwise
    """
    res = jsonify(get_mail(mail_id))
    res.status_code = 200 # Status code for "ok"
    return res

@app.route('/mail/inbox/<recipient>', methods=['GET'])
def get_inbox_route(recipient: str):
    """
    Summary: Gets all mail entries for a recipient from the json file and sends them to the client

    Args:
        recipient (str): The recipient of the mail

    Returns:
        list: A jsonified list of dictionaries representing the mail entries
    """
    res = jsonify(get_inbox(recipient))
    res.status_code = 200
    return res

# TODO: implement a route to get all mail entries for a sender
# HINT: start with soemthing like this:
#   @app.route('/mail/sent/<sender>', ...)
@app.route('/mail/sent/<sender>', methods=['GET'])
def get_sent_route(sender: str):
    """DOCSTRING
    Summary: Gets all mail entries sent by a user and sends them to the client

    Args:
        sender (str): the name of the sender

    Returns:
       list: A jsonified list of dictionaries representing the mail entries 

    """
    res = jsonify(get_sent(sender))
    res.status_code = 200
    return res


if __name__ == '__main__':
    app.run(port=5000, debug=True)
