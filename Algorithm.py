import random
class Algorithm:
    def __init__(self,list_item,list_value,list_weight,size):
        self.list_item = list_item
        self.list_value = list_value
        self.list_weight = list_weight
        self.size = size

    @staticmethod
    def generateItem(size):
        list_item = [
        "Ring",
        "Watch",
        "Purse",
        "Trouser",
        "T-Shirt",
        "Shoes",
        "Glasses",
        "Cosmestics",
        "Laptop",
        "Food",
        "Water bottles",
        "Cell phone",
        "Books"
    ]
        #Lấy 5 sản phẩm ngẫu nhiên
        return random.sample(list_item,size)
    
    @staticmethod
    def generate_Value(size):
        #Tạo 5 giá trị ngẫu nhiên cho 5 sản phẩm
        return [random.randint(1,100) for _ in range(size)]
    
    @staticmethod
    def generate_Weight(size):
        #Tạo 5 khối lượng ngẫu nhiên cho 5 sản phẩm
        return [random.randint(1,10) for _ in range(size)]
    
    def combine_Dictionary(self):
        #Kết hợp sản phẩm : Khối lượng - giá trị
        list_item_value = {item: {"weight": weight, "value" : value} for item,weight,value in zip (self.list_item,self.list_weight,self.list_value)}
        return list_item_value

    def create_individual(self):
        individual = [random.randint(0, 1) for _ in range(len(self.list_item))]
        # Kiểm tra xem danh sách có tất cả giá trị là 0 không
        while all(value == 0 for value in individual):
            individual = [random.randint(0, 1) for _ in range(len(self.list_item))]     
        return individual
    
    def create_population(self, population_size):
        return [self.create_individual() for _  in range (population_size)]
    
    def evaluate_Fitness(self, list_Items, individual, max_weight):
        total_Value = 0
        total_Weight = 0
        for i in range(len(individual)):
            if individual[i] == 1: 
                item = self.list_item[i]  # Lấy tên item từ self.list_item
                total_Value += list_Items[item]["value"]
                total_Weight += list_Items[item]["weight"]
        
        if total_Weight > max_weight: 
            fitness = -1
        else: 
            fitness = total_Value
            
        return fitness


    def evaluate_Population(self,listItems,populations, max_weight):
        fitness_score = []
        for individual in populations:
            fitness = self.evaluate_Fitness(listItems,individual,max_weight)
            fitness_score.append(fitness)
        return fitness_score

    def calculate_Probabilities(self, fitness_scores):
        total_fitness = sum(fitness_scores)
        probabilities = [score / total_fitness for score in fitness_scores]
        return probabilities

    def roulette_wheel_selection(self,populations, probabilities):
        selected_individuals = []
        for _ in range(len(populations)):
            spin = random.random()  # Quay bánh xe để chọn cá thể
            cumulative_probability = 0
            for i, prob in enumerate(probabilities):
                cumulative_probability += prob
                if spin <= cumulative_probability:
                    selected_individuals.append(populations[i])
                    break
        return selected_individuals
    
    def single_PointCrossover(self, parent1, parent2):
        crossover_point = random.randint(1, len(parent1) - 1)  # Chọn điểm cắt ngẫu nhiên
        child1 = parent1[:crossover_point] + parent2[crossover_point:]  # Tạo con 1 từ gen của cha mẹ
        child2 = parent2[:crossover_point] + parent1[crossover_point:]  # Tạo con 2 từ gen của cha mẹ
        return child1, child2

    def crossover_Population(self, selected_Individuals, crossover_rate):
        num_parents = len(selected_Individuals)
        num_offsprings = int(crossover_rate * num_parents)
        offspring_population = []

        for _ in range(num_offsprings // 2):
            parent1 = random.choice(selected_Individuals)  # Chọn ngẫu nhiên cha mẹ 1
            parent2 = random.choice(selected_Individuals)  # Chọn ngẫu nhiên cha mẹ 2
            child1, child2 = self.single_PointCrossover(parent1, parent2)  # Lai ghép
            offspring_population.extend([child1, child2])  # Thêm con vào quần thể con
        return offspring_population
    
    def mutate_Population(self,offspring_Populations,mutation_rate):
        mutated_Individuals = []
        for individual in offspring_Populations:
            copy_individual = list(individual)
            for i in range(len(copy_individual)):
                if random.random() < mutation_rate:
                    copy_individual[i] = 1 if copy_individual[i] == 0 else 0
            mutated_Individuals.append(copy_individual)
        return mutated_Individuals
    
    def print_BestSolution(self, best_solution, list_Items, max_weight):
        best_items = [item for index, item in enumerate(list_Items) if best_solution[index] == 1]
        total_weight = 0
        result = {
            'ItemsSelected': [],
            'TotalValue': None,
            'TotalWeight': None
        }
        print("Items Selected in the Best Solution:")
        for item in best_items:
            item_info = {
                'Item': item,
                'Weight': list_Items[item]['weight'],
                'Value': list_Items[item]['value']
            }
            result['ItemsSelected'].append(item_info)
            total_weight += list_Items[item]['weight']
            print(f"{item}: weight={list_Items[item]['weight']}, value={list_Items[item]['value']}")
        
        result['TotalValue'] = self.evaluate_Fitness(list_Items, best_solution, max_weight)
        result['TotalWeight'] = total_weight

        print("Total Value:", result['TotalValue'])
        print("Total Weight:", result['TotalWeight'])
        return result
        
        
