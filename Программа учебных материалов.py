class EducationalMaterialsLibrary:
    def __init__(self):
        self.resources = {}

    def add_resource(self, name, resource_type, description, url):
        resource = {
            "type": resource_type,
            "description": description,
            "url": url
        }
        self.resources[name] = resource

    def view_resource(self, name):
        resource = self.resources.get(name)
        if resource:
            print(f"Resource: {name}")
            print(f"Type: {resource['type']}")
            print(f"Description: {resource['description']}")
            print(f"URL: {resource['url']}")
        else:
            print(f"Resource '{name}' not found.")

    def search_resources(self, keyword):
        matching_resources = []
        for name, resource in self.resources.items():
            if keyword.lower() in name.lower() or keyword.lower() in resource['description'].lower():
                matching_resources.append(name)
        return matching_resources

    def filter_resources(self, resource_type):
        filtered_resources = []
        for name, resource in self.resources.items():
            if resource['type'].lower() == resource_type.lower():
                filtered_resources.append(name)
        return filtered_resources

# Example usage
library = EducationalMaterialsLibrary()

# Add resources
library.add_resource("Python Basics", "Video Tutorial", "Learn the basics of Python programming.", "https://example.com/python-basics")
library.add_resource("Data Structures in C++", "Textbook", "Learn about data structures in C++.", "https://example.com/data-structures-cpp")

# View a resource
library.view_resource("Python Basics")

# Search for resources
print(library.search_resources("python"))

# Filter resources
print(library.filter_resources("video tutorial"))
