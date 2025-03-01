"""
This is ONLY the framing scripts from video 
"""
import csv
data_dict = {}

rows = []

zero_row = ['video', 'summary', 'opinion', 'claim', 'location', 'tampering', 'AI', 'counter', 'EXPLICIT FRAME']
#Explicit frames in sheet
zero_row.append('Human Trafficking')
zero_row.append('Human Trafficking - Labor')
zero_row.append('Urban Crime')
zero_row.append('Election Fraud')
zero_row.append('Welfare')
zero_row.append('Unsure')

#Implicit frames in sheet
zero_row.append('IMPLICIT FRAME')
zero_row.append('Human Trafficking')
zero_row.append('Human Trafficking - Labor')
zero_row.append('Urban Crime')
zero_row.append('Election Fraud')
zero_row.append('Welfare')
zero_row.append('Unsure')

#Media type 
zero_row.append('TYPE')
zero_row.append('Interview - News Station')
zero_row.append('Interview - Independent')
zero_row.append('News broadcast')
zero_row.append('Person talking to phone (self filmed)')
zero_row.append('Skit')
zero_row.append('Podcasting')
zero_row.append('Illustration')
zero_row.append('Image Carousel')
zero_row.append('Stitch/Duet')
zero_row.append('Greenscreen')
zero_row.append('Narrating other TikTok')
zero_row.append('Cartoon')
zero_row.append('Narrating over images/videos')
zero_row.append('Split screen (spam)')
zero_row.append('Split screen (not spam)')
zero_row.append('Other')
zero_row.append('Unsure')

#CTA
zero_row.append('CTA')
zero_row.append('Share')
zero_row.append('Comment')
zero_row.append('Follow')
zero_row.append('Like')
zero_row.append('Other')

#Text features
zero_row.append('TEXT')
zero_row.append('Text added')
zero_row.append('Subtitles by creator')
zero_row.append('Auto subtitles')

all_rows = []

with open('Coder5.csv', newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	new_row = ['video', 'summary', 'opinion', 'claim', 'location', 'tampering', 'AI', 'counter', 'EXPLICIT FRAME']

	for row in reader:
		new_row = []
		if len(row['video'].split('-')) > 1:
			video = row['video'].split('-')[1]
			new_row.append(video)
			new_row.append(row['summary'])
			new_row.append(row['opinion'])
			new_row.append(row['claim'])
			new_row.append(row['location'])
			new_row.append('') #TODO - Tampering
			new_row.append('') #TODO - AI
			new_row.append(row['orientation'])
			new_row.append("EXPLICIT FRAME")
			rumor = ''
			if type(row['rumor']) is not dict:
				rumor = row['rumor']
			else:
				rumor = row['rumor']['choices']

			#FRAMES - explicit
			if 'Human Trafficking - Not Labor' not in rumor: 
				new_row.append(0)
			else:
				new_row.append(1)

			if 'Human Trafficking - Labor' not in rumor: 
				new_row.append(0)
			else:
				new_row.append(1)

			if 'Urban safety' not in rumor:
				new_row.append(0)
			else:
				new_row.append(1)

			if 'Election Fraud' not in rumor:
				new_row.append(0)
			else:
				new_row.append(1)

			if 'Illegal immigrants getting welfare' not in rumor:
				new_row.append(0)
			else:
				new_row.append(1)

			if 'Unsure' not in rumor:
				new_row.append(0)
			else:
				new_row.append(1)
				
			new_row.append('IMPLICIT FRAME')

			rumor = ''
			if type(row['rumor2']) is not dict:
				rumor = row['rumor2']
			else:
				rumor = row['rumor2']['choices']

			#FRAMES - implicit
			if 'Human Trafficking - Not Labor' not in rumor: 
				new_row.append(0)
			else:
				new_row.append(1)

			if 'Human Trafficking - Labor' not in rumor: 
				new_row.append(0)
			else:
				new_row.append(1)

			if 'Urban safety' not in rumor:
				new_row.append(0)
			else:
				new_row.append(1)

			if 'Election Fraud' not in rumor:
				new_row.append(0)
			else:
				new_row.append(1)

			if 'Illegal immigrants getting welfare' not in rumor:
				new_row.append(0)
			else:
				new_row.append(1)

			if 'Unsure' not in rumor:
				new_row.append(0)
			else:
				new_row.append(1)

			new_row.append("TYPE")

			vid_type = ""

			if type(row['imagetype']) is not dict:
				vid_type = row['imagetype']
			else:
				vid_type = row['imagetype']['choices']

			if 'Interview - News Station' not in vid_type:
				new_row.append(0)
			else:
				new_row.append(1)

			if 'Interview - Independent'not in vid_type:
				new_row.append(0)
			else:
				new_row.append(1)

			if 'News broadcast' not in vid_type:
				new_row.append(0)
			else:
				new_row.append(1)

			if 'Person talking to phone (self filmed)' not in vid_type:
				new_row.append(0)
			else:
				new_row.append(1)

			if 'Skit' not in vid_type:
				new_row.append(0)
			else:
				new_row.append(1)


			if 'Podcasting' not in vid_type:
				new_row.append(0)
			else:
				new_row.append(1)


			if 'Illustration' not in vid_type:
				new_row.append(0)
			else:
				new_row.append(1)

			if 'Image Carousel' not in vid_type:
				new_row.append(0)
			else:
				new_row.append(1)

			if 'Stitch/Duet with another creator' not in vid_type:
				new_row.append(0)
			else:
				new_row.append(1)

			if 'Person using greenscreen' not in vid_type:
				new_row.append(0)
			else:
				new_row.append(1)

			if 'Person narrating over another TikTok (NOT split screen and NOT stitch)' not in vid_type:
				new_row.append(0)
			else:
				new_row.append(1)

			if 'Cartoon' not in vid_type:
				new_row.append(0)
			else:
				new_row.append(1)

			if 'Narrating over images or other videos' not in vid_type:
				new_row.append(0)
			else:
				new_row.append(1)

			if 'Split screen (two videos side by side) where one side is slime, video games, or other strange content' not in vid_type:
				new_row.append(0)
			else:
				new_row.append(1)

			if 'Split screen (two videos side by side)' not in vid_type:
				new_row.append(0)
			else:
				new_row.append(1)

			if 'Other' not in vid_type:
				new_row.append(0)
			else:
				new_row.append(1)

			if 'Unsure' not in vid_type:
				new_row.append(0)
			else:
				new_row.append(1)

			#TODO -- same thing for CTA

			new_row.append("CTA")

			cta = ""

			new_row.append(0)
			new_row.append(0)
			new_row.append(0)
			new_row.append(0)
			new_row.append(0)
			# if type(row['cta']) is not dict:
			# 	cta = row['cta']
			# else:
			# 	cta = row['cta']['choices']


			# if 'This video is asking users to share it ' not in cta:
			# 	new_row.append(0)
			# else:
			# 	new_row.append(1)

			# if 'This video is asking users to comment on it' not in cta:
			# 	new_row.append(0)
			# else:
			# 	new_row.append(1)

			# if 'This video is asking users to follow the creator' not in cta:
			# 	new_row.append(0)
			# else:
			# 	new_row.append(1)

			# if 'This video is asking users to like the video' not in cta:
			# 	new_row.append(0)
			# else:
			# 	new_row.append(1)

			# if 'This video is asking for users to perform another action' not in cta:
			# 	new_row.append(0)
			# else:
			# 	new_row.append(1)

			#TODO -- same thing for text

			new_row.append("TEXT")

			text_vid = ""

			if type(row['videotext']) is not dict:
				text_vid = row['videotext']
			else:
				text_vid = row['videotext']['choices']

			if 'This video has had text added to it' not in text_vid:
				new_row.append(0)
			else:
				new_row.append(1)

			if 'This video has has subtitles added to it by the creator' not in text_vid:
				new_row.append(0)
			else:
				new_row.append(1)

			if 'This video has automated subtitles from TikTok' not in text_vid:
				new_row.append(0)
			else:
				new_row.append(10)

			all_rows.append(new_row)


with open('cleaned5.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(zero_row)
    for r in all_rows:
    	spamwriter.writerow(r)


