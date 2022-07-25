from pytz import NonExistentTimeError


class Network(object):
    """A pyramid network.

    This class represents a pyramid network. The network topology can be loaded
    from a file, and it can find the best arrest scenario to maximize the seized
    asset.

    You may, if you wish, change the API of this class to add extra public
    methods or attributes. Make sure that you do not change the public methods
    that were defined in the handout. Otherwise, you may fail test results for
    those methods.

    """
    # === Attributes ===
    # TODO: Complete this part


    def load_log(self, log_file_name):
        """Load the network topology from the log log_file_name.

        TODO: Complete this part
        """
        #TODO: Complete this part

        file = open(log_file_name, "r")

        for line in file:
            line = line.strip()
            line = line.split("#")

            if len(line) == 2:
                self.name= line[0]
                self.asset = line[1]
                self.children = []

            else:
                
                member = Network()
                member.name = line[0]
                member.asset = line[2]
                member.children = []
                #print(self.search(line[1]).name)
                self.search(line[1]).children.append(member)


    def sponsor(self, member_name):
        """Return the sponsor name of member with name member_name.

        TODO: Complete this part
        """

        #TODO: Complete this part

        for child in self.children:
            if child.name == member_name:
                return self.name

        for child in self.children:
            if child.sponsor(member_name) != None: return child.sponsor(member_name)



    def mentor(self, member_name):
        """Return the mentor name of member with name member_name.

        TODO: Complete this part
        """

        #TODO: Complete this part

        if len(self.children) == 1 and self.children[0].name == member_name: return self.name
        else:
            for i in range (0, len(self.children)):
                if i == 0 and self.children[i].name == member_name: return self.name
                if self.children[i].name == member_name: return self.children[i-1].name

        for child in self.children:
            if child.mentor(member_name) != None: return child.mentor(member_name)

    def assets(self, member_name):
        """Return the assets of member with name member_name.

        TODO: Complete this part
        """

        #TODO: Complete this part
        return self.search(member_name).asset


    def getChildren(self, member_name):
        """Return the name of all children of member with name member_name.

        TODO: Complete this part
        """

        #TODO: Complete this part

        childrenNames =[]
        for child in self.search(member_name).children:
            childrenNames.append(child.name)

        return childrenNames



    def best_arrest_assets(self, maximum_arrest):
        """Search for the amount of seized assets in the best arrest scenario
        that maximizes the seized assets. Consider all members as target zero.

        TODO: Complete this part
        """

        #TODO: Complete this part

    def best_arrest_order(self, maximum_arrest):
        """Search for list of member names in the best arrest scenario that
        maximizes the seized assets. Consider all members as target zero,
        and the order in the list represents the order that members are
        arrested.

        TODO: Complete this part
        """

        #TODO: Complete this part

    def search(self, name):
        if self.name == name:
            return self

        for child in self.children:
            if child.search(name) != None: return child.search(name)





if __name__ == "__main__":
    # A sample example of how to use a network object
    network = Network()
    network.load_log("pyramidScheme/topology1.txt")

    member_name = "Emma"
    print(member_name + "'s sponsor is " + network.sponsor(member_name))

    print(member_name + "'s mentor is " + network.mentor(member_name))
    
    print(member_name + "'s asset is " + str(network.assets(member_name)))
    
    print(member_name + "'s children are " + str(network.getChildren(member_name)))
    """""
    maximum_arrest = 4
    print("The best arrest scenario with the maximum of " + str(maximum_arrest)\
          + " arrests will seize " + str(network.best_arrest_assets(maximum_arrest)))
    print("The best arrest scenario with the maximum of " + str(maximum_arrest)\
          + " arrests is: " + str(network.best_arrest_order(maximum_arrest)))
          """""
