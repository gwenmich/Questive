def render_text(text, font, pos, screen):
    rendered_text = font.render(text, True, "white")
    rendered_txt_rect = rendered_text.get_rect(center=pos)
    screen.blit(rendered_text, rendered_txt_rect)


