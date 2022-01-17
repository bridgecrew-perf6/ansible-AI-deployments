import json, sys, os

def getAgentName(agents):    
    for agent in agents:
        if agent["status"]["inventory"]["hostname"] == "localhost" and  not agent["spec"]["approved"]:
            return agent["metadata"]["name"]
    print ("Error: Agent not found")
    exit(1)

def main():
    try:
        fileName = sys.argv[1]
    except:
        print(f"Error: usage: {os.path.basename(__file__ )} <FILE PATH>")
        exit(1)

    with open(fileName,'r') as f:
        agentJson = json.load(f)

    print (getAgentName(agentJson["resources"]))



if __name__ == "__main__":
    main()
