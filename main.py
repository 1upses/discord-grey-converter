#Copyright (c) 2020, 1ups_ Inc.  All rights reserved.
#Copyrights licensed under the GNU General Public License v3.0.
#See the accompanying LICENSE file for terms.

text_entry = tk.Entry(root, textvariable=text)
text_entry.insert(0, "text")
text_entry.config(fg = 'grey')
text_entry.pack()
text_entry.bind("<FocusIn>", on_focus_in)
text_entry.bind("<FocusOut>", on_focus_out)

image_label = tk.Label(root)
image_label.pack()

submit_button = tk.Button(root, text='Submit', command=on_submit)
submit_button.pack()

root.mainloop()

chaine = "grey-"+filename
im2.save(chaine)
im2.show()