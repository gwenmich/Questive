

class GamePlay:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.game_state_manager = game_state_manager

    def run(self):
        pass


# test data
data = {
    'response_code': 0,
    'results': [
        {'type': 'multiple',
         'difficulty': 'medium',
         'category': 'General Knowledge',
         'question': 'What is the Swedish word for &quot;window&quot;?',
         'correct_answer': 'F&ouml;nster',
         'incorrect_answers': ['H&aring;l', 'Sk&auml;rm', 'Ruta']},

        {'type': 'boolean',
         'difficulty': 'easy',
         'category': 'Science: Computers',
         'question': 'Pointers were not used in the original C programming language; they were added later on in C++.',
         'correct_answer': 'False',
         'incorrect_answers': ['True']}
    ]
}
import pygame

pygame.init()
clock = pygame.time.Clock()
questions = data["results"]
# 3 seconds show category
screen = pygame.display.set_mode((1280, 720))
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill("black")
    small_font = pygame.font.Font("/Users/gwenmichailidis/Coding/Questive/assets/font/PressStart2P-Regular.ttf", 20)
    large_font = pygame.font.Font("/Users/gwenmichailidis/Coding/Questive/assets/font/PressStart2P-Regular.ttf", 30)


    def render_text(text, font):
        rendered_text = font.render(text, True, "white")
        rendered_txt_rect = rendered_text.get_rect(center = (1280 // 2, 200))
        screen.blit(rendered_text, rendered_txt_rect)



    def display_category():
        render_text("Category", small_font)
        render_text(questions[0]["category"], large_font)

    def display_question():
        render_text(questions[0]["question"], small_font)


    display_category()
    pygame.display.update()
    pygame.time.wait(2000)
    # screen.fill("black")
    pygame.display.update()
    display_question()

    pygame.display.update()
    clock.tick(60)

# show questions & buttons with answers
# if wrong lose 1 life and try again?
# if right show page with clue and button click next
# show suspects - click on the ones that match with the clue (ie the suspect had brown hair choose all with brown hair)
# click next question
# repeat until player has chosen one suspect or questions finish and has to choose one
# win or lose
# replay button








if __name__ == "__main__":
    pass
