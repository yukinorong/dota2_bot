from JsonManager.JsonManager import *


def command_manager(order, obj, args):
    print("[command_manager] ", order, obj, args)
    if obj == "user":
        return user_change(order, args)
    # elif obj == "manager":
    #     pass
    #     manager_change(order, args)
    else:
        print("[command_manager] obj error")


def user_create(args):
    ret = None
    try:
        conf = getCustomerInfo()
        conf[args[0]] = {"nickname": args[1], "qq": args[2]}
        setCustomerInfo(conf)
        ret = "ok"
    finally:
        return ret


def user_update(args):
    ret = None
    try:
        conf = getCustomerInfo()
        conf[args[0]] = {"nickname": args[1], "qq": args[2]}
        setCustomerInfo(conf)
        ret = "ok"
    finally:
        return ret


def user_delete(args):
    ret = None
    try:
        conf = getCustomerInfo()
        conf.pop(args[0], None)
        setCustomerInfo(conf)
        ret = "ok"
    finally:
        return ret


def user_search(args):
    ret = None
    try:
        conf = getCustomerInfo()
        ret = conf.pop(args[0], None)
    finally:
        return ret


def user_change(order, args):
    if order == "create":
        return user_create(args)
    elif order == "update":
        return user_update(args)
    elif order == "delete":
        return user_delete(args)
    elif order == "search":
        return user_search(args)
    else:
        print("[user_change] order error")

# todo: 添加管理員權限添加
# def manager_change(order, args):
#     if order == "create":
#         manager_create(args)
#     elif order == "update":
#         manager_update(args)
#     elif order == "delete":
#         manager_delete(args)
#     elif order == "search":
#         manager_search(args)
#     else:
#         print("[manager_change] order error")
