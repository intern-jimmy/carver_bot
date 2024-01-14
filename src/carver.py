from web3 import Web3

ABIS = [{"anonymous": "false", "inputs": [{"indexed": "false", "internalType": "uint8", "name": "version", "type": "uint8"}], "name": "Initialized", "type": "event"},
        {"anonymous": "false", "inputs": [{"indexed": "false", "internalType": "address",
                                           "name": "account", "type": "address"}], "name": "Paused", "type": "event"},
        {"anonymous": "false", "inputs": [{"indexed": "true", "internalType": "address", "name": "stoneAddress", "type": "address"},
                                          {"indexed": "false", "internalType": "address[]",
                                              "name": "requiredResources", "type": "address[]"},
                                          {"indexed": "false", "internalType": "uint32[]",
                                              "name": "requiredQuantities", "type": "uint32[]"},
                                          {"indexed": "false", "internalType": "bool", "name": "active", "type": "bool"}], "name": "RecipeSet", "type": "event"},
        {"anonymous": "false", "inputs": [{"indexed": "true", "internalType": "bytes32", "name": "role", "type": "bytes32"},
                                          {"indexed": "true", "internalType": "bytes32",
                                              "name": "previousAdminRole", "type": "bytes32"},
                                          {"indexed": "true", "internalType": "bytes32", "name": "newAdminRole", "type": "bytes32"}], "name": "RoleAdminChanged", "type": "event"},
        {"anonymous": "false", "inputs": [{"indexed": "true", "internalType": "bytes32", "name": "role", "type": "bytes32"},
                                          {"indexed": "true", "internalType": "address",
                                              "name": "account", "type": "address"},
                                          {"indexed": "true", "internalType": "address", "name": "sender", "type": "address"}], "name": "RoleGranted", "type": "event"},
        {"anonymous": "false", "inputs": [{"indexed": "true", "internalType": "bytes32", "name": "role", "type": "bytes32"},
                                          {"indexed": "true", "internalType": "address",
                                              "name": "account", "type": "address"},
                                          {"indexed": "true", "internalType": "address", "name": "sender", "type": "address"}], "name": "RoleRevoked", "type": "event"},
        {"anonymous": "false", "inputs": [{"indexed": "false", "internalType": "uint256", "name": "workingUntil", "type": "uint256"},
                                          {"indexed": "false", "internalType": "uint256", "name": "awayUntil", "type": "uint256"}], "name": "ShopSetUp", "type": "event"},
        {"anonymous": "false", "inputs": [{"indexed": "true", "internalType": "address", "name": "player", "type": "address"},
                                          {"indexed": "false", "internalType": "address",
                                              "name": "stoneAddress", "type": "address"},
                                          {"indexed": "false", "internalType": "uint256", "name": "quantity", "type": "uint256"}], "name": "StoneCarved", "type": "event"},
        {"anonymous": "false", "inputs": [{"indexed": "false", "internalType": "address",
                                           "name": "account", "type": "address"}], "name": "Unpaused", "type": "event"},
        {"inputs": [], "name":"DEFAULT_ADMIN_ROLE", "outputs":[{"internalType": "bytes32",
                                                                "name": "", "type": "bytes32"}], "stateMutability": "view", "type": "function"},
        {"inputs": [], "name":"MODERATOR_ROLE", "outputs":[{"internalType": "bytes32",
                                                            "name": "", "type": "bytes32"}], "stateMutability": "view", "type": "function"},
        {"inputs": [], "name":"adminSetupShop", "outputs":[],
            "stateMutability":"nonpayable", "type":"function"},
        {"inputs": [], "name":"awayUntil", "outputs":[{"internalType": "uint256",
                                                       "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"},
        {"inputs": [{"internalType": "address", "name": "_stoneAddress", "type": "address"},
                    {"internalType": "uint256", "name": "_quantity", "type": "uint256"}], "name": "carveStone", "outputs": [], "stateMutability":"nonpayable", "type":"function"},
        {"inputs": [], "name":"getAvailability", "outputs":[{"internalType": "uint256", "name": "", "type": "uint256"},
                                                            {"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"},
        {"inputs": [{"internalType": "address", "name": "stoneAddress", "type": "address"}], "name": "getRecipe", "outputs": [{"components": [{"internalType": "address[]", "name": "requiredResources", "type": "address[]"},
                                                                                                                                              {"internalType": "uint32[]", "name": "requiredQuantities", "type": "uint32[]"},
                                                                                                                                              {"internalType": "bool", "name": "active", "type": "bool"}], "internalType": "struct StoneCarver.Recipe", "name": "", "type": "tuple"}], "stateMutability": "view", "type": "function"},
        {"inputs": [{"internalType": "bytes32", "name": "role", "type": "bytes32"}], "name": "getRoleAdmin", "outputs": [
            {"internalType": "bytes32", "name": "", "type": "bytes32"}], "stateMutability": "view", "type": "function"},
        {"inputs": [{"internalType": "bytes32", "name": "role", "type": "bytes32"},
                    {"internalType": "address", "name": "account", "type": "address"}], "name": "grantRole", "outputs": [], "stateMutability":"nonpayable", "type":"function"},
        {"inputs": [{"internalType": "bytes32", "name": "role", "type": "bytes32"},
                    {"internalType": "address", "name": "account", "type": "address"}], "name": "hasRole", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view", "type": "function"},
        {"inputs": [], "name":"initialize", "outputs":[],
            "stateMutability":"nonpayable", "type":"function"},
        {"inputs": [], "name":"minClosedTime", "outputs":[{"internalType": "uint256",
                                                           "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"},
        {"inputs": [], "name":"minOpenTime", "outputs":[{"internalType": "uint256",
                                                         "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"},
        {"inputs": [], "name":"pause", "outputs":[],
            "stateMutability":"nonpayable", "type":"function"},
        {"inputs": [], "name":"paused", "outputs":[{"internalType": "bool",
                                                    "name": "", "type": "bool"}], "stateMutability": "view", "type": "function"},
        {"inputs": [{"internalType": "address", "name": "", "type": "address"}], "name": "recipes", "outputs": [
            {"internalType": "bool", "name": "active", "type": "bool"}], "stateMutability": "view", "type": "function"},
        {"inputs": [{"internalType": "bytes32", "name": "role", "type": "bytes32"},
                    {"internalType": "address", "name": "account", "type": "address"}], "name": "renounceRole", "outputs": [], "stateMutability":"nonpayable", "type":"function"},
        {"inputs": [{"internalType": "bytes32", "name": "role", "type": "bytes32"},
                    {"internalType": "address", "name": "account", "type": "address"}], "name": "revokeRole", "outputs": [], "stateMutability":"nonpayable", "type":"function"},
        {"inputs": [{"internalType": "address", "name": "_stoneAddress", "type": "address"},
                    {"internalType": "address[]",
                        "name": "_requiredResources", "type": "address[]"},
                    {"internalType": "uint32[]",
                        "name": "_requiredQuantities", "type": "uint32[]"},
                    {"internalType": "bool", "name": "_active", "type": "bool"}], "name": "setRecipe", "outputs": [], "stateMutability":"nonpayable", "type":"function"},
        {"inputs": [{"internalType": "uint256", "name": "_minOpenTime", "type": "uint256"},
                    {"internalType": "uint256",
                        "name": "_varOpenTime", "type": "uint256"},
                    {"internalType": "uint256",
                        "name": "_minClosedTime", "type": "uint256"},
                    {"internalType": "uint256", "name": "_varClosedTime", "type": "uint256"}], "name": "setTimes", "outputs": [], "stateMutability":"nonpayable", "type":"function"},
        {"inputs": [], "name":"setUpShop", "outputs":[],
            "stateMutability":"nonpayable", "type":"function"},
        {"inputs": [{"internalType": "bytes4", "name": "interfaceId", "type": "bytes4"}], "name": "supportsInterface", "outputs": [
            {"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view", "type": "function"},
        {"inputs": [], "name":"unpause", "outputs":[],
            "stateMutability":"nonpayable", "type":"function"},
        {"inputs": [], "name":"varClosedTime", "outputs":[{"internalType": "uint256",
                                                           "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"},
        {"inputs": [], "name":"varOpenTime", "outputs":[{"internalType": "uint256",
                                                         "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"},
        {"inputs": [], "name":"workingUntil", "outputs":[{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}]


def carverAwayUntil(rpcAddress, carverAddress):
    w3 = Web3(Web3.HTTPProvider(rpcAddress))
    contract_address = Web3.to_checksum_address(carverAddress)
    contract = w3.eth.contract(contract_address, abi=ABIS)
    carverDataSet(rpcAddress, carverAddress)
    return contract.functions.awayUntil().call()


def carverWorkingUntil(rpcAddress, carverAddress):
    w3 = Web3(Web3.HTTPProvider(rpcAddress))
    contract_address = Web3.to_checksum_address(carverAddress)
    contract = w3.eth.contract(contract_address, abi=ABIS)
    return contract.functions.workingUntil().call()


def carverDataSet(rpc_address, carver_address):
    result = {}
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.to_checksum_address(carver_address)
    contract = w3.eth.contract(contract_address, abi=ABIS)
    result['away_until'] = contract.functions.awayUntil().call()
    result['get_availability'] = contract.functions.getAvailability().call()
    result['min_closed_time'] = contract.functions.minClosedTime().call()
    result['min_open_time'] = contract.functions.minOpenTime().call()
    result['paused'] = contract.functions.paused().call()
    result['var_closed_time'] = contract.functions.varClosedTime().call()
    result['var_open_time'] = contract.functions.varOpenTime().call()
    result['working_until'] = contract.functions.workingUntil().call()

    return result