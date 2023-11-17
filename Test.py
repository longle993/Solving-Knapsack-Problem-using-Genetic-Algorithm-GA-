from Algorithm import Algorithm

#Step 1: Tạo sản phẩm - khối lượng - giá trị
max_weight = 12 #tại giao diện cho người dùng nhập tổng khối lượng túi
size = 5 #tại giao diện cho người dùng nhập số lượng sản phẩm tối thiểu là 5, tối đa là 10
algorithm = Algorithm(Algorithm.generateItem(size),Algorithm.generate_Value(size), Algorithm.generate_Weight(size),10)
list_Items = algorithm.combine_Dictionary()
print("List Items:")
print(list_Items)

#Step 2: Tạo quần thể
size_population = 20 #tại giao diện cho người dùng nhập số lượng quần thể tối thiểu 10 tối đa 30
populations = algorithm.create_population(size_population)
print("\nCreate Populations:")
print(populations)

#Step 3: Đánh giá độ thích nghi
fitness_score = algorithm.evaluate_Population(list_Items,populations,max_weight)
print("\nEvaluate Fitness Score:")
print(fitness_score)

#Step 4: Chọn lọc
probabilities = algorithm.calculate_Probabilities(fitness_score)
selected_Individuals = algorithm.roulette_wheel_selection(populations,probabilities)
print("\nSelected Individuals: ")
print(selected_Individuals)

#Step 5: Lai tạo
