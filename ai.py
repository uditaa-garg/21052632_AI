import random
import numpy as np
from PIL import Image, ImageDraw

# Define the canvas dimensions
width = 400
height = 400

# Define the number of squares in the population
population_size = 50

# Create a blank canvas
canvas = Image.new('RGB', (width, height), (255, 255, 255))

# Create a drawing object
draw = ImageDraw.Draw(canvas)

# Function to draw a square
def draw_square(draw, x, y, size, color):
    draw.rectangle([x, y, x + size, y + size], fill=color)

# Define the population of squares
population = []
for _ in range(population_size):
    x = random.randint(0, width - 20)
    y = random.randint(0, height - 20)
    size = random.randint(10, 50)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    population.append((x, y, size, color))

# Function to evaluate the fitness of an image
def evaluate_fitness(canvas, target_image):
    # Convert images to NumPy arrays for pixel-wise comparison
    canvas_array = np.array(canvas)
    target_array = np.array(target_image)
    diff = np.abs(canvas_array - target_array)
    fitness = np.sum(diff)
    return fitness

# Create a target image (your input image)
target_image = Image.open("ai\pepsi.jpg")

# Main evolution loop (crossover, mutation, selection) goes here

# Render the best square configuration
best_configuration = population[0]  # Replace this with your selection logic
x, y, size, color = best_configuration
draw_square(draw, x, y, size, color)

# Save the generated image to a file
canvas.save('generated_image.png')
