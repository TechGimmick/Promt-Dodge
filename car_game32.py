import pygame
import random
import sys
pygame.init()
# Get screen dimensions
infoObject = pygame.display.Info()
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (128, 128, 128)
GREEN = (0, 128, 0)  

# Initialize the screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Car Race Game")


def car_game():
    # Car dimensions
    CAR_WIDTH, CAR_HEIGHT = 100, 100

    # Obstacle dimensions
    OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 100, 100

    # Tree dimensions
    TREE_WIDTH, TREE_HEIGHT = 50, 50

    # Road dimensions
    ROAD_WIDTH = WIDTH // 2 + 100
    ROAD_HEIGHT = HEIGHT

    

    # Load car images
    car_images = [pygame.image.load(f'BOXY CAR{i}.png') for i in range(1, 10)]
    car_img = pygame.image.load('BOXY CAR10.png')

    # Load other images
    obstacle_img = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
    obstacle_img.fill(RED)
    tree_img = pygame.image.load('Tree.png')  # Load your tree image here

    # Clock for controlling the frame rate
    clock = pygame.time.Clock()

    # Game variables
    car_x = WIDTH // 2 - CAR_WIDTH // 2
    car_y = HEIGHT - CAR_HEIGHT - 20
    car_speed = 5
    obstacles = []
    trees = []
    tree_speed = 5
    score = 0

    def draw_road():
        pygame.draw.rect(screen, GREY, (WIDTH // 4 - 50, 0, ROAD_WIDTH, ROAD_HEIGHT))

    def draw_car(x, y, car_image):
        screen.blit(car_image, (x, y))

    def draw_obstacles(obstacles):
        for obstacle in obstacles:
            screen.blit(obstacle[2], (obstacle[0], obstacle[1]))

    def draw_trees(trees):
        for tree in trees:
            screen.blit(tree_img, (tree[0], tree[1]))

    def move_obstacles(obstacles):
        for obstacle in obstacles:
            obstacle[1] += car_speed

    def move_trees(trees):
        for tree in trees:
            tree[1] += tree_speed

    def generate_obstacle():
        x = random.randint(WIDTH // 4 - 50, WIDTH // 4 + ROAD_WIDTH - OBSTACLE_WIDTH - 50)
        y = -OBSTACLE_HEIGHT
        car_image = random.choice(car_images)
        obstacles.append([x, y, car_image])

    def generate_trees():
        # Randomly generate trees outside the road bounds
        # Left side
        x_left = random.randint(0, WIDTH // 4 - TREE_WIDTH)
        y_left = random.randint(-TREE_HEIGHT, HEIGHT - TREE_HEIGHT)
        trees.append([x_left, y_left])
        
        # Right side
        x_right = random.randint(WIDTH // 4 + ROAD_WIDTH, WIDTH - TREE_WIDTH)
        y_right = random.randint(-TREE_HEIGHT, HEIGHT - TREE_HEIGHT)
        trees.append([x_right, y_right])

    # Main game loop
    running = True
    while running:
        screen.fill(GREEN)  # Changed background color

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Keyboard input handling
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_x > WIDTH // 4 - 50:
            car_x -= car_speed
        if keys[pygame.K_RIGHT] and car_x < WIDTH // 4 + ROAD_WIDTH - CAR_WIDTH - 50:
            car_x += car_speed

        # Move obstacles and trees
        move_obstacles(obstacles)
        move_trees(trees)

        # Generate new obstacles
        if random.randint(1, 100) < 3:
            generate_obstacle()

        # Generate new trees
        if random.randint(1, 100) < 5:
            generate_trees()

        # Draw road
        draw_road()

        # Draw obstacles
        draw_obstacles(obstacles)

        # Draw trees
        draw_trees(trees)

        # Draw car
        draw_car(car_x, car_y, car_img)  # You can choose any car image here

        # Collision detection
        for obstacle in obstacles:
            if obstacle[1] > HEIGHT:
                obstacles.remove(obstacle)
            elif car_x < obstacle[0] + OBSTACLE_WIDTH and car_x + CAR_WIDTH > obstacle[0] and car_y < obstacle[1] + OBSTACLE_HEIGHT and car_y + CAR_HEIGHT > obstacle[1]:
                print("Game Over!")
                running = False

        # Update the display
        pygame.display.flip()
        clock.tick(60)

    # pygame.quit()
    # sys.exit()

# import pygame
# import random
# import sys

# Initialize Pygame
pygame.init()

# Get screen dimensions
infoObject = pygame.display.Info()
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h

# Set up the screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Engineering Quiz Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)

# Fonts
font = pygame.font.Font(None, 35)

# Engineering prompts and answers
prompts = [
    ("You want to watch a funny movie on Netflix. Which prompt is best?", {
        "options": ["Show me all movies", "Find comedy movie", "Search popular movies"],
        "correct_answer": "Find comedy movie"
    }),
    ("What are the best ways to save for retirement? Which prompt is most helpful?", {
        "options": ["Information on saving", "Financial advice", "List investment options"],
        "correct_answer": "Information on saving"
    }),
    ("Who is Charles Darwin, and what is he known for? Which prompt is ideal?", {
        "options": ["Summary of Darwin", "Famous scientists", "Books on evolution"],
        "correct_answer": "Summary of Darwin"
    }),
    (""" You're searching for vegetarian recipes that are quick and easy to make for a weeknight dinner.
      Which prompt is most suitable?""", {
        "options": ["Show me delicious vegetarian meals.", "Find easy vegetarian recipes for weeknight dinners.", " Search for healthy cooking tips for beginners."],
        "correct_answer": "Find easy vegetarian recipes for weeknight dinners."
    }),
    (" You want to compare the features and specifications of two specific phones: iPhone 15 and Samsung Galaxy S23. Which prompt is best?", {
        "options": ["List all the latest smartphones available.", "Search for reviews of the best smartphones in the market.", "Compare the features of iPhone 15 and Samsung Galaxy S23."],
        "correct_answer": "Compare the features of iPhone 15 and Samsung Galaxy S23."
    }),
    ("What are the NBA teams participating in the playoffs this year? Which prompt is most appropriate?", {
        "options": ["You're interested in learning about the upcoming basketball playoffs and the participating teams.", " Show me live sports events", " Search for information about the history of basketball."],
        "correct_answer": "You're interested in learning about the upcoming basketball playoffs and the participating teams."
    }),
    ("ou're planning a solo backpacking trip through Southeast Asia and are looking for budget-friendly accommodations and unique cultural experiences. Which prompt is best?", {
        "options": ["Find the cheapest flights to Southeast Asia.", "Show me popular tourist attractions in Southeast Asia.", "Suggest affordable backpacking routes in Southeast Asia with unique cultural experiences. "],
        "correct_answer": "Suggest affordable backpacking routes in Southeast Asia with unique cultural experiences. "
    }),
    ("You're interested in finding classic novels with strong female protagonists written by female authors in the 19th century. Which prompt is most suitable?", {
        "options": ["Recommend classic novels featuring strong female leads, written by women authors in the 19th century.", " List all classic novels published in the 19th century.", " Search for famous books with female characters. "],
        "correct_answer": "Recommend classic novels featuring strong female leads, written by women authors in the 19th century.  "
    }),
    ("You're researching the potential applications of artificial intelligence in healthcare. Which prompt is most effective?", {
        "options": ["What is artificial intelligence?", " Search for recent breakthroughs in the field of AI.", " Explore how artificial intelligence is being used to improve healthcare outcomes."],
        "correct_answer": "Explore how artificial intelligence is being used to improve healthcare outcomes."
    }),
    ("You're looking for a specific brand of sustainable clothing that offers ethical production practices and uses recycled materials. You remember the brand name starts with 'P' and is known for its minimalist designs. Which prompt is ideal?", {
        "options": ["Show me all ethical clothing brands.", " Find the 'P' brand known for minimalist designs and ethical production using recycled materials.", "Search for sustainable clothing websites with recycled materials."],
        "correct_answer": "Find the \"P\" brand known for minimalist designs and ethical production using recycled materials."
    }),
    ("You're creating a playlist for a focus session that requires concentration and improved memory. You're looking for instrumental music with calming melodies and minimal lyrics. Which prompt is best suited?", {
        "options": ["Show me all instrumental music playlists.", " Search for music that helps with studying and concentration.", "Recommend instrumental music playlists with calming melodies and minimal lyrics, ideal for focus and memory improvement."],
        "correct_answer": "Recommend instrumental music playlists with calming melodies and minimal lyrics, ideal for focus and memory improvement."
    }),
    ("You're writing a business proposal for a marketing campaign targeting Gen Z consumers. You want to understand their online behavior, preferred communication channels, and buying habits. Which prompt is most helpful?", {
        "options": ["Research the online behavior and buying habits of Gen Z consumers, including their preferred communication channels.", " Find information about marketing strategies for young adults. ", "  Search for trends in online marketing campaigns for different demographics. "],
        "correct_answer": "Research the online behavior and buying habits of Gen Z consumers, including their preferred communication channels."
    }),
    ("You're considering investing in a specific company and want to compare its historical financial performance with its major competitors in the same industry. Which prompt is most effective?", {
        "Options": ["Show me the stock price history of the company.","Search for financial analysis reports of the company.","Compare the historical financial performance of [company name] with its main competitors in the [industry] industry."],
        "correct_answer":"Compare the historical financial performance of [company name] with its main competitors in the [industry] industry."
    }
    ),
    ("You're writing a research paper on the ethical implications of artificial intelligence and want to find scholarly articles that discuss specific potential risks and biases in AI development. Which prompt is most suitable",{
        "Options": ["Identify peer-reviewed scholarly articles addressing the ethical concerns and potential biases surrounding AI development.","Search for recent research on artificial intelligence.","Find articles about the benefits and challenges of AI."],
        "correct_answer":"Identify peer-reviewed scholarly articles addressing the ethical concerns and potential biases surrounding AI development."
    }),
    ("You're experiencing unusual symptoms and want to find reliable medical information to understand potential causes and identify relevant specialists for consultation. Which prompt is most helpful?",{
        "Options": ["Search for online symptom checkers and medical advice websites.","Describe my symptoms and suggest possible causes, including relevant medical specialties for further evaluation.","Find information about common illnesses and their treatment options."],
        "correct_answer":"Describe my symptoms and suggest possible causes, including relevant medical specialties for further evaluation."
    }),
    ("You're facing a legal issue related to intellectual property rights and need to find relevant case studies and legal precedents involving copyright infringement in the technology sector. Which prompt is most appropriate?",{
        "Options": ["Search for information about intellectual property laws.","Identify relevant legal precedents and case studies involving copyright infringement in the technology sector."," Find resources on how to protect copyrights online. "],
        "correct_answer":"Identify relevant legal precedents and case studies involving copyright infringement in the technology sector."
    }),
    ("You're planning a multi-city trip across Europe with specific interests in historical landmarks, local cuisines, and hidden gems off the beaten path. Which prompt is most suitable?",{
        "Options": ["Search for Python libraries for data analysis."," Find tutorials on learning Python programming basics.","Identify Python code snippets and documentation examples for data manipulation and machine learning algorithms using specific libraries."],
        "correct_answer":"Identify Python code snippets and documentation examples for data manipulation and machine learning algorithms using specific libraries."
    }),
    ("You're researching the artistic movement of Surrealism for a university assignment, focusing on the works of Salvador Dalí and the techniques he employed to create his dreamlike landscapes. Which prompt is most appropriate?",{
        "Options": ["Search for information about the history of Surrealism.","Analyze the techniques employed by Salvador Dalí in his Surrealist paintings, particularly focusing on how he created dreamlike landscapes.","Show me famous paintings from the Surrealist movement."],
        "correct_answer":"Analyze the techniques employed by Salvador Dalí in his Surrealist paintings, particularly focusing on how he created dreamlike landscapes."
    }),
    ("You're writing a scientific paper on the potential applications of nanotechnology in environmental remediation. You need to find recent research articles exploring the use of nanomaterials for specific environmental challenges like water pollution cleanup. Which prompt is most effective?",{
        "Options": ["Find information about the benefits and risks of nanotechnology.","Identify recent research articles exploring the use of specific nanomaterials in environmental remediation, especially for water pollution cleanup.","Search for recent discoveries in the field of nanotechnology."],
        "correct_answer":"Identify recent research articles exploring the use of specific nanomaterials in environmental remediation, especially for water pollution cleanup."
    }),
    ("You're developing a social media marketing campaign for a new sustainable clothing brand targeting environmentally conscious millennials. You want to understand their preferred social media platforms, content formats, and messaging styles. Which prompt is most helpful?",{
        "Options": ["Research the online behavior of millennials on social media."," Find marketing strategies for promoting eco-friendly products.","Analyze the social media behavior of environmentally conscious millennials, including their preferred platforms, content formats, and messaging styles relevant to a new sustainable clothing brand."],
        "correct_answer":"Analyze the social media behavior of environmentally conscious millennials, including their preferred platforms, content formats, and messaging styles relevant to a new sustainable clothing brand."
    }),
    ("You're a financial advisor managing a client's investment portfolio and want to identify alternative investment options with low correlation to traditional asset classes like stocks and bonds. You're particularly interested in exploring real estate investment trusts (REITs) and venture capital funds. Which prompt is most suitable?",{
        "Options": ["Identify low-correlation alternative investment options with a focus on real estate investment trusts (REITs) and venture capital funds, suitable for diversifying a client's portfolio beyond traditional asset classes."," Search for alternative investment options for diversifying portfolios."," Find information about real estate investment trusts and venture capital funds."],
        "correct_answer":"Identify low-correlation alternative investment options with a focus on real estate investment trusts (REITs) and venture capital funds, suitable for diversifying a client's portfolio beyond traditional asset classes."
    }),
    ("You're leading a research project on the impact of social media on adolescent mental health. You need to access scholarly articles and data sets that explore the correlation between specific social media usage patterns and mental health outcomes in teenagers. Which prompt is most effective?",{
        "Options": [" Search for research on the effects of social media on teenagers.","Identify peer-reviewed research articles and data sets exploring the correlation between specific social media usage patterns in adolescents and their mental health outcomes."," Find articles on the positive and negative impacts of social media."],
        "correct_answer":"Identify peer-reviewed research articles and data sets exploring the correlation between specific social media usage patterns in adolescents and their mental health outcomes."
    }),
    ("You're a medical professional treating a patient with a complex medical condition and need to find clinical trials investigating new and innovative treatment options for the specific diagnosis. Which prompt is most appropriate?",{
        "Options": ["Search for clinical trials for [patient's condition.","Find information about the latest treatment options for [patient's condition].","Identify ongoing clinical trials investigating new and innovative treatment options for [patient's specific diagnosis], considering their eligibility criteria and potential benefits."],
        "correct_answer":"Identify ongoing clinical trials investigating new and innovative treatment options for [patient's specific diagnosis], considering their eligibility criteria and potential benefits."
    }),
    ("You're a medical professional treating a patient with a complex medical condition and need to find clinical trials investigating new and innovative treatment options for the specific diagnosis. Which prompt is most appropriate?",{
        "Options": ["Search for clinical trials for [patient's condition.","Find information about the latest treatment options for [patient's condition].","Identify ongoing clinical trials investigating new and innovative treatment options for [patient's specific diagnosis], considering their eligibility criteria and potential benefits."],
        "correct_answer":"Identify ongoing clinical trials investigating new and innovative treatment options for [patient's specific diagnosis], considering their eligibility criteria and potential benefits."
    })
    

    

    # Add more prompts here
]

# Function to display prompts and check answers
def display_prompt(current_score, prompt_data):
    prompt, data = prompt_data
    options = data["options"]
    correct_answer = data["correct_answer"]
    
    text = font.render(prompt, True, BLACK)
    text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//4))
    
    option_texts = [font.render(option, True, BLACK) for option in options]  # Convert option strings to surfaces
    
    option_rects = []
    option_spacing = 7  # Adjust this value to control vertical spacing
    total_option_height = sum(option_text.get_height() for option_text in option_texts) + (len(option_texts) - 1) * option_spacing
    start_y = (HEIGHT - total_option_height) // 2
    
    for i, option_text in enumerate(option_texts):
        # Adjusting the x-coordinate to center the text horizontally
        option_rect = option_text.get_rect(midleft=(WIDTH//4, start_y + i * (option_text.get_height() + option_spacing)))
        option_rects.append(option_rect)
    
    selected_option = None
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(option_rects):
                    if rect.collidepoint(event.pos):
                        selected_option = i
                        if options[selected_option] == correct_answer:
                            current_score += 1
                            return current_score
                        else:
                            current_score = 0
                            return current_score
        
        screen.fill(WHITE)
        screen.blit(text, text_rect)
        for option_text, option_rect in zip(option_texts, option_rects):
            pygame.draw.rect(screen, GRAY, option_rect)
            screen.blit(option_text, option_rect)
        
        pygame.display.flip()

# Function to display game over message and retry option
def game_over():
    game_over_text = font.render("Wrong answer! Retry? (Y/N)", True, RED)
    game_over_rect = game_over_text.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.blit(game_over_text, game_over_rect)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return True
                elif event.key == pygame.K_n:
                    return False

# Function to display level complete message
def level_complete(level):
    level_complete_text = font.render(f"Level {level} complete! Press any key to continue.", True, GREEN)
    level_complete_rect = level_complete_text.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.blit(level_complete_text, level_complete_rect)
    pygame.display.flip()
    pygame.time.wait(2000)  # Wait for 2 seconds
    pygame.event.clear()  # Clear any pending events
    pygame.event.wait()  # Wait for a new event

# Main game loop
current_level = 1
score = 0
conti = True
prompt_index = 0  # Index to iterate through prompts sequentially

while conti:
    car_game()
    while True:
        screen.fill(WHITE)  # Clear the screen
        print(score)
        score = display_prompt(score, prompts[prompt_index])
        # Display question and answer
        if not score:
            if not game_over():
                conti = False
                break

        # Move to the next prompt
        prompt_index = (prompt_index + 1) % len(prompts)

        if score == 3:  # If user answered three questions correctly
            score = 0
            break  # Move to the next level