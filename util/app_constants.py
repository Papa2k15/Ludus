import string
import json


deployment_db = 'pg.db'

alpha_list = list(string.ascii_uppercase)
num_list = list(string.digits)
user_pre = 'pg_'
start = 0
end = 2
char_bit = 0
user_id_length = 15

#HELPERS
_des_ = 'description'
_code_ = 'code'


#Request Error Codes
class pg_responses(object):
    INV_LOGIN = {'code':'pg_1','description':"Invalid username and password."}
    REG_SUCCES = {'code':'pg_2','description':"Registration Success."}
    REG_FAILED = {'code':'pg_3','description':"Registration Failed."}
    EMAIL_IN_USE = {'code':'pg_4','description':"Email is already in use."}
    USERNAME_IN_USE = {'code':'pg_5','description':"Username is already in use."}
    UNK_ERROR  = {'code':'pg_error','description':"Something went wrong, please try again."}

class logging_events(object):
    #USER EVENT
    AUTH_LOGIN_SUCCESS = {'description':"Authenticated user successfully logged in.",'code':100}
    AUTH_LOGIN_FAILURE = {'description':"Authenticated user failed login.",'code':101}
    UNAUTH_LOGIN_ATTEMPT = {'description':"Unauthorized user login attempt.",'code':102}
    AUTH_LOGOUT_SUCCESS = {'description':"Authorized user logged out successfully.",'code': 103}
    REG_SUCCESS = {'description':"User successfully registered.",'code': 108}
    REG_FAILED = {'description':"User registration failed.",'code': 109}
    #COMMAND EVENT
    COMMAND_UPDATE = {'description':"Admin user updated a command successfully.",'code': 125}
    COMMAND_FAILED_UPDATE = {'description':"Admin user failed to update a command.",'code': 126}
    #CONFIG EVENT
    CONFIG_CREATE = {'description':"Admin user created initial config.",'code': 150}
    CONFIG_FAILED_CREATE = {'description':"Admin user failed to create initial config.",'code': 151}
    CONFIG_UDPATE = {'description':"Admin user updated config.",'code': 152}
    CONFIG_FAILED_UPDATE = {'description':"Admin user failed to update config.",'code': 153}
    #PROJECT EVENT
    PROJECT_CREATE = {'description':"User created a new project.",'code': 200}
    PROJECT_FAILED_CREATE = {'description':"User failed to create a new project.",'code': 201}
    PROJECT_UPDATE = {'description':"User updated an existing project.",'code': 202}
    PROJECT_FAILED_UPDATE = {'description':"User failed to update an existing project.",'code': 203}
    PROJECT_REMOVED = {'description':"User removed a project.",'code': 204}
    PROJECT_FAILED_REMOVE = {'description':"User failed to remove a project.",'code': 205}
    TASK_CREATE = {'description':"User created a new task.",'code': 206}
    TASK_FAILED_CREATE = {'description':"User failed to create a task.",'code': 207}
    TASK_UPDATE = {'description':"User updated an existing task.",'code': 208}
    TASK_FAILED_UPDATE = {'description':"User failed to update task.",'code': 209}
    TASK_REMOVE = {'description':"User removed a task.",'code': 210}
    TASK_FAILED_REMOVE = {'description':"User failed to remove an existing task.",'code': 211}
    #EVENTS EVENT 
    EVENT_CREATE = {'description':"User created a new event.",'code': 250}
    EVENT_FAILED_CREATE = {'description':"User failed to create a new event.",'code': 251}
    EVENT_REMOVE = {'description':"User removed an event.",'code': 252}
    EVENT_FAILED_REMOVE = {'description':"User failed to remove an existing event.",'code': 253}