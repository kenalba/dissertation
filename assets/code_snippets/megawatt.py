#!/usr/bin/python
# coding: utf-8
#
# Megawatt, copyright (c) 2014, 2018 Nick Montfort <nickm@nickm.com>
#
# Copying and distribution of this file, with or without modification, are
# permitted in any medium without royalty provided the copyright notice and
# this notice are preserved. This file is offered as-is, without any warranty.
#
# Updated 31 May 2018, changed "print" and "/" for Python 2 & 3 compatibility
# Updated 26 November 2018, substituted a shorter all-permissive license
# Written 29 November 2014

"""_Megawatt_ is the title of both a computer program, the source code
to which you may be reading, and the output of this program, which in
many ways is like a standard novel and which you may instead be reading.
This note appears at the beginning of both.

The program _Megawatt_ is based on passages from Samuel Beckett’s novel
_Watt,_ first published in 1953 but written much earlier, when Beckett
was aiding the French Resistance during World War II.

The novel _Megawatt_ leaves aside all of the more intelligible language
of Beckett’s novel and is based, instead, on that which is most systematic
and inscrutable. It does not just recreate these passages, although with
minor changes the _Megawatt_ code can be used to do so. In the new novel,
rather, they are intensified by generating, using the same methods that
Beckett used, significantly more text than is found in the already
excessive _Watt_.

To produce the novel in markdown format, run megawatt.py (a Python 2
program) with TextBlob (a text processing library) installed.

    % python megawatt.py > megawatt.text

To produce PDF and epub documents, use pandoc:

    % pandoc -V geometry:paperwidth=5.5in \
        -V geometry:paperheight=8.25in \
        -V geometry:margin=.7in -o megawatt.pdf \
        megawatt.text
    % echo '% Megawatt' > info.txt
    % echo '% Nick Montfort' >> info.txt
    % pandoc -o megawatt.epub info.txt megawatt.text

_Megawatt_ was written/generated for the second NaNoGenMo (National
Novel Generation Month) in November 2014, and is free software."""

__author__ = 'Nick Montfort'
__license__ = 'ISC'
__version__ = '1.0'


#### GENERAL

from textblob import Word

def next_section(num):
    text.append('\n\\newpage')
    text.append('\n# ' + num + '\n\n')

text = []
spelled_out = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty'
}


#### THE VOICES

text.append('\n# I\n\n')
def combine(num, words):
    final = []
    if num > 0 and len(words) >= num:
        if num == 1:
            final = final + [[words[0]]]
        else:
            final = final + [[words[0]] +
                    c for c in combine(num - 1, words[1:])]
        final = final + combine(num, words[1:])
    return final

## In Watt the voices = ['sang', 'cried', 'stated', 'murmured']
## And Watt understood = ['all', 'much', 'little', 'nothing']
## Here the voices did eight things and there are eight levels:
voices = ['sang', 'cried', 'stated', 'murmured', 'babbled', 'chattered',
          'ranted', 'whispered']
understood = ['all', 'most', 'much', 'half', 'little', 'less', 'bits',
              'nothing']
para = ''
preface = ', and sometimes they '
for num in range(len(voices)):
    for word_list in combine(num + 1, voices):
        para = para + preface + ' and '.join(word_list)
        if len(word_list) == 1:
            para = para + ' only'
para = ('Watt heard voices. Now these voices,' + para[5:] +
    ', all together, at the same time, as now, to mention ' +
    'only these ' + spelled_out[len(voices)] + ' kinds of voices, for ' +
    'there were others. And sometimes Watt understood ' +
    ', and sometimes he understood '.join(understood) + ', as now.')
text.append(para)


#### WAY OF ADVANCING

next_section('II')
## In Watt there is only one direction, compass = ['east']
## Also, the phrase 'for example' appears in Watt; the new text seems
## exhaustive, so this is omitted.
compass = ['east', 'southeast', 'south', 'southwest', 'west',
           'northwest', 'north', 'northeast']
leg = ['right', 'left']
j = 0
rl = 0
for i in range(len(compass)):
    para = (['Watt’s', 'His'][i > 0] + ' way of advancing due ' +
           compass[0]  + ' was')
    for j in range(8):
        para = para + (' to turn his bust as far as possible towards the ' +
        compass[[6, 2][rl]] + ' and at the same time to fling his ' + leg[rl] +
        ' leg as far as possible towards the ' + compass[[2, 6][rl]] +
        ', and then')
        rl = [1, 0][rl]
        para = para + ['', ' again', ' once again', ' yet again'][int(j/2)]
    para = (para[:-14] + 'so on, over and over again, many many times, ' +
            'until he reached his destination, and could sit down.')
    text.append(para)
    compass = compass[1:] + compass[:1]


#### ENTERING THE HOUSE

next_section('III')
text.append('The house was in darkness.')
## In Watt there are two doors = ['front ', 'back ']
## Watt visits them and returns, went = ['went', 'returned']
## Here there are four doors and Watt visits them twice as many times:
doors = ['front ', 'back ', 'side ', 'trap']
went = ['went', 'returned', 'again returned', 'once more returned']
for i in range(len(doors) * 4):
    para = ('Finding the ' + doors[0] + 'door locked, Watt ' +
            went[int(i/len(doors))] + ' to the ')
    doors = doors[1:] + doors[:1]
    para = para + (doors[0] + 'door.')
    text.append(para)
text[-1] = text[-1][:-50] + 'now open, Watt was able to enter the house.'


#### THE SHORT STATEMENT

next_section('IV')
text.append('Inside were Mr Knott and Erskine and another. Before ' +
            'leaving, this gentleman made the following short statement:')
para = 'And the poor old lousy earth, my earth'
def ancestor(depth):
    if depth < 1:
        yield ''
    else:
        for parent in [' father’s', ' mother’s']:
            for grandparent in list(ancestor(depth - 1)):
                yield parent + grandparent
for possessive in ['my', 'other people’s']:
## Originally this is done for three generations, i.e.:
#   for i in range(1,4)
## Here the number of generations are doubled, so there are six:
    for i in range(1,7):
        elders = ancestor(i)
        for elder in list(elders):
            para = para + ' and ' + possessive + elder
para = para + '.'
text.append(para)


#### COMPOSITION OF THE DISH

next_section('V')
def various_kinds(word, sense, plural=False):
    items = []
    for synset in Word(word).synsets[sense - 1].hyponyms():
        next_name = synset.lemma_names()[0].replace('_', ' ')
        if plural:
            items.append(Word(next_name).pluralize())
        else:
            items.append(next_name)
    return (', '.join(items) + ', and other ' + Word(word).pluralize() +
            ' of various kinds, ')
text.append('On Saturday night a sufficient quantity of food was ' +
               'prepared and cooked to carry Mr Knott through the week.')
para = 'This dish contained foods of various kinds, '
## The original begins: 'such as soup of various kinds, fish, eggs, game,
## poultry, meat, cheese, fruit, all of various kinds...'
para = para + various_kinds('soup', 1)
para = para + various_kinds('fish', 2)
para = para + 'and eggs of various kinds, '
para = para + various_kinds('game', 4)
para = para + various_kinds('poultry', 1)
para = para + various_kinds('meat', 1)
para = para + various_kinds('cheese', 1)
para = para + various_kinds('fruit', 1)
para = para + various_kinds('bread', 1)
para = para + various_kinds('butter', 1)
para = para + 'and absinthe, mineral water, '
para = para + various_kinds('tea', 1)
para = para + various_kinds('coffee', 1)
para = para + various_kinds('milk', 1)
para = para + various_kinds('beer', 1)
para = para + 'whiskey, brandy, '
para = para + various_kinds('wine', 1)
para = para + ('and water, and it contained also many things to take ' +
              'for the good of the health, such as insulin, digitalin, ' +
              'calomel, iodine, laudanum, mercury, coal, iron, ' +
              'camomille, worm-powder, ')
para = para + various_kinds('medicine', 2, plural=True)
para = para + ('and of course salt and mustard, pepper and sugar, and of ' +
               'course a little salicylic acic, to delay fermentation.')
text.append(str(para))


#### PORTION OF THE DISH CONSUMED

next_section('VI')
## In Watt only half (here, ten twentieths) is mentioned.
para = ('Mr Knott was never heard to complain of his food, though he ' +
        'did not always eat it. Sometimes he emptied the bowl, scraping ' +
        'its sides, and the bottom, with the trowel, until they shone, ' +
        'and sometimes he left one twentieth of it,')
for numerator in range(2,20):
    para = para + ' or ' + spelled_out[numerator] + ' twentieths of it,'
para = para + ' or some other fraction, and sometimes he left the whole of it.'
text.append(para)


#### PERHAPS HE FELT

next_section('VII')
## In Watt there are three feelings:
# feelings = ['calm', 'free', 'glad']
## Here extended to six:
feelings = ['calm', 'free', 'glad', 'whole', 'fine', 'right']
para = ('But in the stress... Not that Watt felt ' + ' and '.join(feelings) +
       ', for he had never done so. But he thought that perhaps he felt ')
for i in range(6, 0, -1):
    next_feelings = ''
    for c in combine(i, feelings):
        next_feelings = next_feelings + ' and '.join(c) + ', or '
    para = (para + next_feelings + 'if not ' + next_feelings[:-4] +
               ' at least ')
para = para[:-9] + 'without knowing it.'
text.append(para)


#### MR KNOTT'S FOOTWEAR
## 'As for his feet, sometimes he wore on each a sock ...'
## Not expanded. ppg256-7 is based on this passage:
## http://nickm.com/poems/ppg256.html

#### MR KNOTT'S MOVEMENTS
## '... from the door to the window, from the window to the door ...'
## Not expanded. Nanowatt computationally produces it in English and French:
## http://nickm.com/post/2013/11/nanowatt/

#### ARRANGEMENTS OF MR KNOTT'S FURNITURE
## '... on the Sunday, the tallboy on its feet by the fire ...'
## Not expanded. Nanowatt computationally produces it in English and French:
## http://nickm.com/post/2013/11/nanowatt/


#### MR KNOTT'S PHYSICAL APPEARANCE

next_section('VIII')
## Only the first four are in the original.
attributes = [
    ['thin', 'sturdy', 'fat'],
    ['small', 'middlesized', 'tall'],
    ['pale', 'yellow', 'flushed'],
    ['dark', 'ginger', 'fair'],
    ['brown-eyed', 'blue-eyed', 'hazel-eyed'],
    ['ectomorphic', 'mesomorphic', 'endomorphic'],
    ['clean-shaven', 'bearded', 'moustached'],
    ['erect', 'stooped', 'leaning']
]
def permute(list_of_lists):
    if len(list_of_lists) == 1:
        for i in list_of_lists[0]:
            yield 'and ' + i
    else:
        for i in list_of_lists[0]:
            for j in permute(list_of_lists[1:]):
                yield i + ', ' + j
para = ('With regard to the so important matter of Mr Knott’s physical ' +
        'appearance, Watt had unfortunately little or nothing to say. ' +
        'For one day Mr Knott would be ')
para = para + ', and the next '.join(list(permute(attributes)))
para = (para + ', or so it seemed to Watt, to mention only the figure, ' +
        'stature, skin, hair, eyes, body type, facial hair, and posture.')
text.append(para)


#### THE END

next_section('IX')
text.append(('&nbsp;' * 16) + '?') # These lacunae appear often in Watt.
text.append('They parted.')
text.append(('&nbsp;' * 32) + '?')


####  EVERYTHING TO STDOUT

blank = '\\thispagestyle{empty}\n\n\\newpage\n\n&nbsp;\n\n'
half_title = ('&nbsp;\n\n&nbsp;\n\n&nbsp;\n\n# Megawatt\n\n' + (blank * 2))
title = ('&nbsp;\n\n&nbsp;\n\n&nbsp;\n\n# Megawatt\n\n' +
         '&nbsp;\n\n&nbsp;\n\n&nbsp;\n\n## Nick Montfort' +
         '\n&nbsp;\n&nbsp;\n&nbsp;\n\n__A novel__  \n' +
         '__computationally, deterministically generated__  \n' +
         '__extending passages from Samuel Beckett’s *Watt*__  \n&nbsp;  \n' +
         '&nbsp;  \n__Bad Quarto / Cambridge, Massachusetts__' +
         (blank * 2))
preface = '# Preface\n\n' + __doc__ + (blank * 2)
print(half_title + title + preface)
print('\\setcounter{page}{1}\n\n' + '\n\n'.join(text))
this_file = open('megawatt.py')
print('\n\\newpage\n\n')
print('# Addenda\n\n\n\\scriptsize\n\n')
print('    ' + '    '.join(list(this_file)))
