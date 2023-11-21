from Algorithm import Algorithm

# Setup
crossover_rate = 0.9
mutation_rate = 0.1

# Step 1: Tạo sản phẩm - khối lượng - giá trị
max_weight = 12 
size = 5 
algorithm = Algorithm(Algorithm.generateItem(size), Algorithm.generate_Value(size), Algorithm.generate_Weight(size), size)
list_Items = algorithm.combine_Dictionary()
print("List Items:")
print(list_Items)

# Step 2: Tạo quần thể
size_population = 20 
populations = algorithm.create_population(size_population)
print("\nCreate Populations:")
print(populations)

# Step 7: Lặp lại quá trình và chọn cá thể tốt nhất
num_generations = 10 
best_solution = None 

for generation in range(num_generations):
    fitness_score = algorithm.evaluate_Population(list_Items, populations, max_weight)
    probabilities = algorithm.calculate_Probabilities(fitness_score)
    selected_individuals = algorithm.roulette_wheel_selection(populations, probabilities)
    offspring_population = algorithm.crossover_Population(selected_individuals, crossover_rate)
    mutation_Populations = algorithm.mutate_Population(offspring_population, mutation_rate)
    
    # Kiểm tra nếu danh sách đột biến không rỗng trước khi chọn cá thể tốt nhất
    if mutation_Populations:
        best_individual = max(mutation_Populations, key=lambda x: algorithm.evaluate_Fitness(list_Items, x, max_weight))
        
        if best_solution is None or algorithm.evaluate_Fitness(list_Items, best_individual, max_weight) > algorithm.evaluate_Fitness(list_Items, best_solution, max_weight):
            best_solution = best_individual
    else:
        print("\nNo valid individuals after mutation.")

    # Gán quần thể mới từ quần thể sau khi đột biến
    populations = mutation_Populations

# In ra cá thể tốt nhất cuối cùng
print("\nBest Solution found:")
algorithm.print_BestSolution(best_solution,list_Items,max_weight)
