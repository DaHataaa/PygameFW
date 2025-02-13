# PygameFW beta-0.1
It's a simple framework for pygame, that includes buttons, scales, sliders and etc.

README-file in progress...


## Classes:
### PygameFW.Button()
	Arguments:
		id, x, y, dx, dy, mode,
		border_size, color_border, color_border_covered, color_border_selected,
		color_fill, color_fill_covered, color_fill_selected,
		text,
		icon, icon_covered, icon_selected,
		visible


### PygameFW.Scale()
	Arguments:
		id, x, y, dx, dy,
		value, value_max,
		direction,
		no_border, border_size,
		color_border, color_fill, color_filled,
		visible

### PygameFW.Slider()
	Arguments:
		id, x, y, dx, dy,
		value, value_max,
		direction,
		no_border, border_size, color_border,
		color_fill, color_filled,
		circle_size, color_circle, color_circle_covered, color_circle_selected,
		visible

### PygameFW.Text()
	Arguments:
		id, x, y,
		font_size, color, value, font,
		visible