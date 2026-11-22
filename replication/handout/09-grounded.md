# Skills Lexicon pilot, grounded run: message 10 of 13 (chunk 09, 5 concepts)

Everything you need is in this message. Don't fetch, search or look anything up. Draft only from what is here and what you already know.

**Independence.** Several models are drafting these same 36 entries separately so Nik Bear Brown can compare them. Don't read, search for or ask for any other model's drafts, including Claude's. The material below is source material only (the lexicon's record, candidate neighbors, posting snippets, Wikipedia, Wikidata and WordNet candidates); it holds no one's drafts.

**How to work.** Treat each concept on its own, as if you had never seen the others: don't carry a decision, a wording or a relation from one concept to the next. This is the **grounded** run: each concept comes with its candidate Wikipedia articles, Wikidata items and WordNet senses.

**Instructions for every concept** (use them exactly as written):

~~~~text
You draft entries for Skills Lexicon, an open vocabulary of skills, knowledge areas, abilities, languages, and credentials used to match job postings with course syllabi. You receive one concept and a bundle of source material. You return one JSON object.

Your job is to record what the sources support, not to complete a template. An empty relation list is a correct answer. A plausible relation you cannot support is an error.

Work through these steps in order.

1. Work sense. Read the concept record and the usage examples. Write one sentence saying what the concept means as a job requirement or learning outcome. Every later decision is about this sense.

2. Source links. For Wikipedia, Wikidata, and WordNet separately, pick the single candidate that matches the work sense, or abstain by setting choice to null. Abstain when no candidate matches, when the candidates describe a different sense, or when you cannot tell. Give a one-sentence reason either way. You may cite only sources you linked, plus Wikidata ancestors of the item you linked.

3. Definition. Write one to three sentences in your own words describing the concept as it appears in postings and syllabi. Never reuse more than eight consecutive words from any source. Cite the pointers that support it.

4. Variants. List surface forms that name this concept: abbreviations, alternate spellings, historical names. If a form names the concept only in some contexts, state the condition (for example, "when it labels a skill, role, or team, not the experience itself").

5. Relations. Use only these types, and include a relation only if its test passes with the actual names filled in:
   - synonym: the target can replace the concept in a posting or syllabus without changing what is asked for or taught.
   - hypernym: "[concept] is a kind of [target]" is true.
   - hyponym: "[target] is a kind of [concept]" is true.
   - meronym: practicing or knowing the concept routinely includes the target as a component.
   - holonym: the concept is routinely a component of the target.
   - uses: the concept is typically practiced with the target, which is a tool, runtime, framework, or other technology rather than a component.
   - requires: the target must be learned before the concept can be practiced.
   - certifies: only when the concept is a credential; the credential attests to the target.
   - contrast: the target is often confused with the concept but differs from it. Use this for false-equivalence risks, including look-alike names.
   Do not record antonyms or pertainyms. Work concepts almost never have them.

6. Basis. Give every definition, variant, and relation a basis:
   - "source": the provided material states it, and you give at least one pointer that identifies the exact statement, synset relation, passage, or example.
   - "model_knowledge": you believe it, but the provided material does not state it. This is allowed. Never label model knowledge as source, and never invent a pointer.

7. Targets. If a relation's target matches a concept in lexicon_neighbors, set target_id to that concept's id. Otherwise set target_id to null and proposed_new to true.

8. Final check. Before returning, review every claim. Remove any relation whose test fails when read with the real names, any pointer that does not say what you claim, and anything you added only because a slot was empty. Put any concern a reviewer should see (conflicting sources, unclear sense, a likely error in the lexicon's existing record) in flags.

Pointer formats:
- Wikidata statement: wd:QID#PID=VALUE_QID (for example, wd:Q100#P279=Q200)
- Wikidata label or alias: wd:QID#alias=TEXT
- WordNet lemma: wn:SYNSET_ID#lemma=TEXT
- WordNet relation: wn:SYNSET_ID#RELATION=TARGET_SYNSET_ID, where RELATION is hypernym, hyponym, part_meronym, part_holonym, member_meronym, or member_holonym
- Wikipedia passage: wp:REVISION_ID#quote=TEXT, where TEXT is copied exactly from the provided article and is at most 20 words
- Usage example: ex:EXAMPLE_ID

Return only this JSON object, with no preamble and no code fences:

{
  "concept_id": "string",
  "work_sense": "string",
  "links": {
    "wikipedia": {"choice": "REVISION_ID or null", "reason": "string"},
    "wikidata": {"choice": "QID or null", "reason": "string"},
    "wordnet": {"choice": "SYNSET_ID or null", "reason": "string"}
  },
  "definition": {"text": "string", "basis": "source or model_knowledge", "pointers": ["string"]},
  "variants": [
    {"text": "string", "condition": "string or null", "basis": "source or model_knowledge", "pointers": ["string"]}
  ],
  "relations": [
    {"type": "one of the nine types above", "target_label": "string", "target_id": "string or null", "proposed_new": false, "basis": "source or model_knowledge", "pointers": ["string"], "note": "string or null"}
  ],
  "flags": ["string"]
}
~~~~

**Before you answer**, check every draft against this list and fix what fails (one pass of fixes, no more):

- `links.wikipedia`, `links.wikidata` and `links.wordnet` each have a `choice`, and each is null or one of that concept's candidates below.
- The definition, each variant and each relation has `basis` `source` or `model_knowledge`, and every `source` claim has at least one pointer.
- Every pointer resolves in the material below: `wd:` names the linked item or one of its ancestors and the statement or alias is really there; `wn:` names the linked synset and the lemma or relation is really there; `wp:` names the linked article's revision id and quotes at most 20 words that appear word for word; `ex:` names an example below.
- Only the nine relation types. A `target_id` must be one of that concept's neighbors.
- `certifies` only when the concept's `kind` is `credential`.
- The definition shares no run of 9 or more consecutive words with any Wikipedia text below.

**What to send back.** One JSON object per concept, one per line, in the order below, each with one extra field:
`"_meta": {"model": "<your model and version>", "run": "grounded", "chunk": "09", "attempts": 1}`.
If you can make files, send a file named `drafts-grounded-09.jsonl`. Otherwise send one code block marked `jsonl` holding the 5 lines and nothing else. A script will check them afterwards.

---

## Concept 1 of 5: Teamwork (`tz7ipk5s96`)

~~~~text
Concept record:
{
 "id": "tz7ipk5s96",
 "preferred_name": "Teamwork",
 "kind": "skill",
 "broad_class": "skill",
 "variants": [
  {
   "label": "Team-working"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "kut5s14k79",
  "name": "Collaboration"
 },
 {
  "id": "gisypzf6gf",
  "name": "Communication"
 },
 {
  "id": "nb236cqujn",
  "name": "Coordination"
 },
 {
  "id": "fjheonyp0m",
  "name": "Monitoring"
 },
 {
  "id": "c6mr2nxzm3",
  "name": "Problem solving"
 },
 {
  "id": "pk7cebmtg6",
  "name": "Python"
 },
 {
  "id": "yegnhni99h",
  "name": "Adaptability"
 },
 {
  "id": "xe2d2jfa1r",
  "name": "Application programming interface"
 },
 {
  "id": "gk12ir4ef9",
  "name": "BASIC"
 },
 {
  "id": "ls6hrpynv0",
  "name": "Java"
 },
 {
  "id": "mdcx7ximpo",
  "name": "LESS"
 },
 {
  "id": "mcz3zs6q84",
  "name": "Physics"
 },
 {
  "id": "hjzieo2ohv",
  "name": "React"
 },
 {
  "id": "crm3w31oq7",
  "name": "Team-oriented"
 },
 {
  "id": "hecagq35qn",
  "name": "Nette"
 },
 {
  "id": "g6t643lbht",
  "name": "Microsoft Bot Framework"
 },
 {
  "id": "fnhev4v1dn",
  "name": "Computer networking"
 },
 {
  "id": "ft1f82qoac",
  "name": "AWS networking"
 },
 {
  "id": "y6729eqjad",
  "name": "Red teaming"
 },
 {
  "id": "dv5vi280tf",
  "name": "E-marketing"
 },
 {
  "id": "rdtwc1bnps",
  "name": "Speaking"
 },
 {
  "id": "wkbsvthe6e",
  "name": "Threat modeling"
 },
 {
  "id": "w522rsvq3h",
  "name": "Network peering"
 },
 {
  "id": "t6ptjyq1kp",
  "name": "Time Sharing"
 },
 {
  "id": "a2ymv23g4x",
  "name": "Team leadership"
 },
 {
  "id": "wroqa3tbb6",
  "name": "SWIFT network"
 },
 {
  "id": "rvb4xaqyno",
  "name": "Embalming"
 },
 {
  "id": "npja9s70lb",
  "name": "Repairing"
 },
 {
  "id": "hllkkrms0o",
  "name": "Reporting"
 },
 {
  "id": "dua32jm4h0",
  "name": "Theano"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "scrapifier/indeed-usa-job-postings@v1/indeed_usa_job_postings.csv:8",
  "source": "kaggle:scrapifier/indeed-usa-job-postings (CC0: Public Domain), column description",
  "text": "Job title: Sales Associate/Customer Service Representative (Bilingual/Spanish). Bilingual, Retail sales transactions, Commission pay, Retail customer service procedures, Spanish, Customer communication, Paid training, Teamwork, Received goods storage, Promoting products, Hourly pay, Sales, Customer service, Store closing procedures, Merchandising, Email, Moving, Store opening p…"
 },
 {
  "id": "mohityd2007/real-world-job-postings-dataset-for-ml-projects@v1/jobs_data.csv:90",
  "source": "kaggle:mohityd2007/real-world-job-postings-dataset-for-ml-projects (Attribution 4.0 International (CC BY 4.0)), column Job Description",
  "text": "Job title: Business Development Trainee. Leadership,Team Management,Negotiation,MS-Excel,Coordination,Lead Generation,Teamwork,"
 },
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:94",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: AI Engineer (Middle Level) (Thu Nhập 20-30 Triệu). [\"Python\", \"Git\", \"LangChain\", \"Teamwork\", \"AI\", \"AI\"]"
 },
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:2435",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Machine Learning Analyst. Java, Python, React, SQL, RESTful API, Soft Skills: Communication, Problem-solving, Teamwork, Adaptability, Education-Related Skills: Java, Python, React, Experience-Related Skills: SQL, RESTful API, Communication, Problem-solving, Teamwork, Adaptability"
 },
 {
  "id": "priyankamalavade/naukri-jobs-details@v1/naukri_data_analyst_jobs.csv:1707",
  "source": "kaggle:priyankamalavade/naukri-jobs-details (MIT), column Description",
  "text": "Job title: Education Analyst - Physics. Physics, Edtech, Content Creation, Communication Skills, Content Generation, Artificial Intelligence, Problem Solving, Teamwork"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[
 {
  "title": "Teamwork",
  "revision_id": "1378654751",
  "matched_by": "title",
  "text": "Teamwork is the collaborative effort of a group to achieve a common goal or to complete a task in an effective and efficient way. Teamwork is seen within the framework of a team, which is a group of interdependent individuals who work together towards a common goal.\n\nThe four key characteristics of a team include a shared goal, interdependence, boundedness, stability, the ability to manage their own work and internal process, and operate in a bigger social system.\n\nTeams need to be able to leverage resources to be productive (i.e. playing fields or meeting spaces, scheduled times for planning, guidance from coaches or supervisors, support from the organization, etc.), and clearly defined roles within the team in order for everyone to have a clear purpose. Teamwork is present in contexts including an industrial organization (formal work teams), athletics (sports teams), a school (classmates working on a project), and the healthcare system (operating room teams). In each of these settings, the level of teamwork and interdependence can vary from low (e.g. golf, track and field), to intermediate (e.g. baseball, football), to high (e.g. basketball, soccer), depending on the amount of communication, interaction, and collaboration present between team members.\n\nAmong the requirements for effective teamwork are an adequate team size. The context is important, and team sizes can vary depending upon the objective. A team must include at least two members, and most teams range in size from two to 100. Sports teams generally have fixed sizes based upon set rules, and work teams may change in size depending upon the phase and complexity of the objective.\n\nHistory\n\nThe Oxford English Dictionary records the use of \"team-work\" in the context of a team of draught animals as early as 1800.\n\nEven though collaborative work among groups of individuals is very prominent today, that was not the case over half a century ago. The shift from the typical assembly line to organizational models that contained increasing amounts of teamwork first came about during World War I and World War II, in an effort for countries to unite their people. The movement towards teamwork was mostly due to the Hawthorne studies, a set of studies conducted in the 1920s and 1930s that suggested positive aspects of teamwork in an organizational setting. After organizations recognized the value of teamwork and the positive effects it had on companies, entire fields of work shifted from the typical assembly line to the contemporary High Performance Organizational Model.\n\nEffective teamwork characteristics\n\nA team must have certain interrelated characteristics to work effectively.\n\nAmong these is strong group cohesion. There is a positive relationship between group cohesion and performance.\n\nCommunication is another vital characteristic for effective teamwork. Members must be able to effectively communicate with each other to overcome obstacles, resolve conflict, and avoid confusion. Communication increases cohesion.\n\nCommunication helps to clearly define the team's purpose so that there is a common goal. Having a common goal increases cohesion because all members are striving for the same objective and will help each other achieve their goals.\n\nCommitment occurs when members are focused on achieving the team's common goal.\n\nAccountability is necessary to ensure milestones are reached and that all members are participating. Holding members accountable increases commitment within team relations.\n\nBasic team dynamics\n\nBasic team dynamics include:\n\nOpen communication to avoid conflicts.\n\nEffective coordination to avoid confusion and the overstepping of boundaries.\n\nEfficient cooperation to perform the tasks in a timely manner and produce the required results, especially in the form of workload sharing.\n\nHigh levels of interdependence to maintain trust, risk-taking, and performance.\n\nThese teamwork conditions lead to the team turning in a finished product. To measure if the teamwork was effective, the organization must examine the quality of the output, the process, and the members' experience. The teamwork can be deemed efficient if the output met or exceeded the organization's standard, the process the team chose to take helped them reach their goals, and the members report high levels of satisfaction with the team members as well as the processes that the team followed.\n\nProcesses\n\nTeams perform various processes during different periods of time. The processes can be performed when the team is undertaking specific activities, when the team is changing from one activity to the next, and during both periods of change and action when addressing relationships between the team members. Teamwork processes fall into three categories:\n\nTransition processes\n\nThese processes occur between periods of action. Team members can evaluate their overall performance as a team and on an individual level, give feedback to each other, make clarifications about the upcoming tasks, and make any changes that would improve the process of collaborating.\n\nTask Analysis\n\nGoal Specification\n\nStrategy Formulation\n\nResult oriented group\n\nAction processes\n\nThese processes take place when the team takes steps to accomplish its goals and objectives. Team members keep each other informed about their progress and their responsibilities, while helping one another with tasks. Feedback and collaborative work continues in high levels throughout this process.\n\nMonitoring progress toward goals\n\nSystems Monitoring\n\nTeam Monitoring and Backup Behavior\n\nCoordination\n\nInterpersonal processes\n\nThese processes are present in both action periods and transition periods, and occur between team members. This is a continuous process, in which team members communicate thoughts and/or feelings concerning either another team member or a manner in which a task is being performed. Furthermore, team members encourage and support each other on their individual tasks.\n\nConflict management\n\nMotivation and Confidence building\n\nAffect Management\n\nTeamwork performance generally improves when a team passes through these processes, since processes like these enhance coordination and communication between the team members and therefore increase teamwork and collaborative work.\n\nTraining to improve teamwork\n\nTeamwork and performance can be enhanced through specific training that targets individual team members and the team as a whole. Bruce Tuckman proposed a team developmental model that separated the stages of a team's lifespan and the level of teamwork for each stage:\n\nForming\n\nThis stage is described by approach/avoidance issues, as well as internal conflicts about being independent vs. wanting to be a part of the team.\n\nTeam members usually tend to 'play it safe' and minimize their risk-taking in case something goes wrong.\n\nTeamwork in this stage is at its lowest levels.\n\nStorming\n\nThe second stage is characterized by a competition for power and authority, which is the source of most of the conflicts and doubts about the success of the team.\n\nIf teamwork is low in this stage, it is very unlikely that the team will get past their conflicts. If there is a high degree of teamwork and willingness to collaborate, then the team might have a brighter future.\n\nNorming\n\nThe third stage is characterized by increasing levels of solidarity, interdependence, and cohesiveness, while simultaneously making an effort to adjust to the team environment.\n\nThis stage shows much higher levels of teamwork that make it easier for the above characteristics to occur.\n\nPerforming\n\nThis final stage of team development includes a comfortable environment in which team members are effectively completing tasks in an interdependent and cohesive manner.\n\nThis stage is characterized by the highest levels of comfort, success, interdependence, and maturity, and therefore includes the highest levels of teamwork.\n\nEnhancing teamwork\n\nOne way organizational psychologists measure teamwork is through the Knowledge, Skills, and Abilities (KSA) Teamwork Test. This test was developed by Michael Stevens and Michael Campion in 1994. It assesses people who want to join a team by measuring 14 KSA requirements for teamwork, especially within formal teams. The test has two main categories: Interpersonal KSAs that contain items such as Conflict Resolution and Communication, and Self-Management KSAs that include items such as Goal Setting and Task Coordination.\n\nTeamwork can be enhanced through team development interventions (TDIs) such as leadership training, team training, team debriefing, and team building. These TDIs improve communication, coordination, cooperation, and conflict management within teams. Promoting a sense of community among the team members through efforts such as group events also contributes to the enhancement of teamwork.\n\nLeadership and teamwork\n\nLeaders should establish trust with their teams and provide mutual encouragement to support team success. Leaders can model collaborative behavior to demonstrate effective teamwork to their teams. Team leaders should be both task- and relationship-oriented to facilitate relationships that enhance teamwork. Leaders should ensure that the team member identify and understand their roles and responsibilities within the team. A successful team aligns it objectives with the organization’s vision and goals. Leaders are responsible for inspiring and motivating teams to facilitate the alignment of their objectives with those of the organization.\n\nDrawbacks and benefits\n\nUtilizing teamwork is sometimes unnecessary and can lead to teams not reaching their performance peak. Some of those disadvantages include:\n\nSocial loafing: This phenomenon appears when a person working in a group puts in less effort than they can towards a task. If other members of the team are exerting comparatively more effort, this can create conflict and lead to lower levels of performance.\n\nBehavioral conflicts or ingrained individualism: Employees at higher organizational levels have adapted to positions that require more individual initiative, and therefore have trouble engaging in collaborative work. This creates a more competitive environment with less communication and more conflict. This disadvantage is mostly seen in organizations that utilize teamwork in an extremely hierarchical environment.\n\nIndividual tasks: Certain tasks do not require teamwork, and are more appropriate for individual work. By assigning a team to complete an 'individual task', there can be high levels of conflict between members which can damage the team's dynamic and weaken their overall performance.\n\nGroupthink: This is a psychological phenomenon that occurs within a group of people when, from a desire for conflict-avoidance, the desire for cohesiveness is greater than the desire for the best decisions. When a team experiences groupthink, alternative solutions will not be suggested due to fear of rejection or disagreement within the group. Group members will measure success based on the harmony of their group and not by the outcome of their decisions. One way to counteract groupthink is to have members of a group be from diverse backgrounds and have different characteristics (gender, age, nationality). Another way to avoid groupthink is to require each member to suggest different ideas.\n\nWorking in teams has also shown to be very beneficial. Some advantages of teamwork include:\n\nProblem solving: A group of people can bring together various perspectives and combine views and opinions to rapidly and effectively solve an issue. Due to the team's culture, each team member has a responsibility to contribute equally and offer their unique perspective on a problem to arrive at the best possible solution. Teamwork can lead to better decisions, products, or services. The effectiveness of teamwork depends on the following six components of collaboration among team members: communication, coordination, balance of member contributions, mutual support, effort, and cohesion.\n\nHealthy competition: This can motivate people and help the team excel.\n\nRelationship development: A team that continues to work together will eventually develop an increased level of bonding. This can help members avoid unnecessary conflicts since they have become well acquainted with each other through teamwork. By building strong relationships between members, team members' satisfaction with their team increases, therefore improving both teamwork and performance.\n\nIndividual qualities: Every team member can offer their unique knowledge and ability to help improve other team members. Through teamwork the sharing of these qualities allows team members to be more productive in the future.\n\nMotivation: Working collaboratively can lead to increased motivation levels within a team due to increasing accountability for individual performance. When groups are being compared, members tend to become more ambitious to perform better. Providing groups with a comparison standard increases their performance level thus encouraging members to work collaboratively.\n\nPaulus describes additional benefits of teamwork:\n\nshared workload\n\nopportunity to achieve leadership and social satisfaction\n\nsense of belonging to a successful team\n\nability to accomplish more than if team members worked individually\n\nReferences"
 },
 {
  "title": "Teamwork (sculpture)",
  "revision_id": "1361419812",
  "matched_by": "title-minus-qualifier",
  "text": "Teamwork is a public sculpture by Omri Amrany located at American Family Field west of downtown Milwaukee, Wisconsin. It is cast in bronze and honors Jeffrey Wischer, William DeGrave, and Jerome Starr, the three Iron Workers Local 8 members killed by the Big Blue Crane collapse during the construction of the baseball stadium in 1999. The sculpture was commissioned by the Habush, Habush and Rottier Charitable Foundation for $250,000.\n\nDescription\n\nTeamwork depicts three Milwaukee Local Union 8 Ironworkers dressed for construction work. All wear jeans, t-shirts, boots and hardhats. One holds a clipboard.\n\nInformation\n\nThe sculpture honors William DeGrave, Jerome Starr and Jeffrey Wischer, three ironworkers who were killed by a piece of the stadium's retractable roof that fell when a heavy lift crawler crane failed during the construction of Miller Park (now American Family Field) in July 1999. The widows of the workers, Marjorie DeGrave, Ramona Dulde-Starr and Patricia Wischer, settled a lawsuit against crane-maker Mitsubishi Heavy Industries of America, for an undisclosed total of over $99 million. Attorney Robert L. Habush represented two of the widows in their suit.\n\nReferences"
 },
 {
  "title": "Teamwork (project management)",
  "revision_id": "1359555952",
  "matched_by": "title-minus-qualifier",
  "text": "Teamwork.com is an Irish, privately owned, web-based software company headquartered in Cork, Ireland. Teamwork creates task management and team collaboration software. Founded in 2007, as of 2016 the company stated that its software was in use by over 370,000 organisations worldwide (including Disney, Spotify and HP), and that it had over 2.4m users.\n\nHistory\n\nPeter Coppinger and Dan Mackey founded a company, Digital Crew, in 2007. This company built websites, intranets and custom web-based solutions for clients in Cork, Ireland. Frustrated by whiteboards and software management tools, Coppinger wanted a software system that would help manage client projects and which would be easy to use and generic enough to be used by different types of companies. Originally 37signals Basecamp users themselves, Coppinger and Mackey were frustrated by the limited feature set, and by Basecamp's apparent inaction on their feedback. In October 2007, Coppinger and Mackey launched Teamwork Project Manager, nicknamed TeamworkPM. In March 2015, this was renamed as Teamwork Projects.\n\nIn 2014, after two years of negotiations, TeamworkPM bought the domain name 'Teamwork.com' for US$675,000 (€500,000). At the time this was one of the most expensive domain name purchases by an Irish company, and involved the transfer of a domain name which had been dormant since it was first acquired by the original owner in 1999.\n\nIn 2015, Teamwork.com was named by Gartner to be one of their \"Cool Vendors\" in the Program and Portfolio Management Category. This was followed by the launch of a new real-time messaging product, Teamwork Chat, in January 2015. In June 2015, the company announced a drive to recruit for 40 positions by the end of the year. This was followed by the announcement that the company was investing more than €1 million in a new office, and had leased office space in Park House, Blackpool. \n\nIn June 2016, Teamwork.com undertook a further recruitment drive to entice developers to Cork.\n\nIn July 2021, the company announced that it had raised an investment of $70 million (€59.1 million) from venture capital firm Bregal Milestone to fund further growth.\n\nProducts\n\nTeamwork markets a number of cloud-based applications, including Teamwork, Teamwork Desk, Teamwork Spaces, Teamwork CRM and Teamwork Chat. Teamwork was launched on 4 October 2007, at which time it had time management, milestone management, file sharing, time tracking, and messaging features.\n\nTeamwork's platform reportedly integrates with martech software like HubSpot, as well as other productivity tools like Slack, G Suite, MS Teams, Zapier, Dropbox and QuickBooks.\n\nAwards\n\nIn 2016, Teamwork was awarded Cork's Best SME in the Cork Chamber of Commerce \"Company of the Year\" awards.\n\nIn 2016, Teamwork was named number 7 in Deloitte's Fast 50 tech companies hit €1.6bn turnover.\n\nIn 2015, Teamwork was identified as a Gartner \"Cool Vendor\" in the Program and Portfolio Management Category.\n\nSee also"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q626225",
  "label": "teamwork",
  "description": "collaborative effort of a team to achieve a common goal",
  "aliases": [
   "team work",
   "teamwork in the workplace"
  ],
  "claims": {
   "P31": [
    "Q15910354"
   ],
   "P279": [
    "Q1145523"
   ]
  },
  "revision_id": "2565908090",
  "value_labels": {
   "Q15910354": "soft skills",
   "Q1145523": "collaboration"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q7691687",
  "label": "Teamwork",
  "description": "artwork by Omri Amrany",
  "aliases": [],
  "claims": {
   "P31": [
    "Q860861"
   ]
  },
  "revision_id": "2570777022",
  "value_labels": {
   "Q860861": "sculpture"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q22909287",
  "label": "Teamwork",
  "description": "project management software",
  "aliases": [
   "teamwork",
   "Teamwork Hq",
   "TeamworkHQ",
   "Teamworkcom",
   "Teamwork Projects",
   "Teamwork Desk",
   "Teamwork Chat",
   "teamwork.com",
   "teamworkpm",
   "teamworkpm.net",
   "teamworkdesk.com"
  ],
  "claims": {
   "P31": [
    "Q167035",
    "Q474157",
    "Q1391080",
    "Q84177695",
    "Q43229"
   ]
  },
  "revision_id": "2571821236",
  "value_labels": {
   "Q167035": "project management software",
   "Q474157": "collaborative software",
   "Q1391080": "business software",
   "Q84177695": "to-do list manager",
   "Q43229": "organization"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q15910354",
  "label": "soft skills",
  "description": "skills which are desirable in all professions",
  "aliases": [
   "common skills",
   "core skills",
   "soft skill"
  ],
  "claims": {
   "P279": [
    "Q205961"
   ]
  },
  "revision_id": "2540342691",
  "ancestor_of": "Q626225",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1145523",
  "label": "collaboration",
  "description": "the process of two or more people, groups, or organizations working together to achieve a common goal, share knowledge, and create value",
  "aliases": [
   "coproduction",
   "collaborative effort",
   "collaborating"
  ],
  "claims": {
   "P279": [
    "Q1914636"
   ],
   "P1889": [
    "Q156744"
   ]
  },
  "revision_id": "2559431386",
  "ancestor_of": "Q626225",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q205961",
  "label": "skill",
  "description": "learned ability and competence to carry out an action",
  "aliases": [
   "athletic ability"
  ],
  "claims": {
   "P31": [
    "Q110403031"
   ],
   "P279": [
    "Q1347367",
    "Q9081"
   ],
   "P527": [
    "Q7535186",
    "Q15910354",
    "Q2480597"
   ],
   "P460": [
    "Q460693",
    "Q1813993",
    "Q7535186",
    "Q121788669"
   ],
   "P1889": [
    "Q21767554"
   ]
  },
  "revision_id": "2567571464",
  "ancestor_of": "Q626225",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1914636",
  "label": "activity",
  "description": "series of actions done by an agent which results in an external change of state",
  "aliases": [
   "act",
   "action",
   "operation",
   "doing",
   "do",
   "acting",
   "practice",
   "db:Process",
   "dol:Process",
   "dul:Process",
   "gfo:Process"
  ],
  "claims": {
   "P31": [
    "Q116505632"
   ],
   "P279": [
    "Q3249551",
    "Q141187917",
    "Q141222018"
   ],
   "P527": [
    "Q4026292",
    "Q52948",
    "Q24902509"
   ],
   "P460": [
    "Q1656682"
   ],
   "P1889": [
    "Q4026292",
    "Q12737077",
    "Q192581",
    "Q3249551",
    "Q142215789"
   ]
  },
  "revision_id": "2572268874",
  "ancestor_of": "Q626225",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q860861",
  "label": "sculpture",
  "description": "three-dimensional work of art",
  "aliases": [
   "sculptures",
   "piece of sculpture",
   "sculptural work",
   "sculptural piece"
  ],
  "claims": {
   "P31": [
    "Q116474095"
   ],
   "P279": [
    "Q8205328",
    "Q4502142",
    "Q17537576",
    "Q35459920",
    "Q350268"
   ],
   "P1889": [
    "Q11634",
    "Q17310537",
    "Q350268"
   ]
  },
  "revision_id": "2558177998",
  "ancestor_of": "Q7691687",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q116474095",
  "label": "type of work of art",
  "description": "Wikidata metaclass",
  "aliases": [
   "type of art work"
  ],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q1437361",
    "Q133449656"
   ],
   "P1889": [
    "Q110452794",
    "Q56055944",
    "Q1437361"
   ]
  },
  "revision_id": "2545044217",
  "ancestor_of": "Q7691687",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q8205328",
  "label": "artificial physical object",
  "description": "physical object made or shaped by humans",
  "aliases": [
   "artifact",
   "man-made physical object",
   "artefact",
   "human-made physical object",
   "non-natural physical object",
   "physical artefact"
  ],
  "claims": {
   "P31": [
    "Q111360549"
   ],
   "P279": [
    "Q223557",
    "Q16686448",
    "Q386724",
    "Q136490012",
    "Q141756646"
   ],
   "P361": [
    "Q11042"
   ],
   "P1889": [
    "Q220659",
    "Q231515",
    "Q16686448",
    "Q136490012"
   ]
  },
  "revision_id": "2567164850",
  "ancestor_of": "Q7691687",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q4502142",
  "label": "visual artwork",
  "description": "work of art that is primarily visual",
  "aliases": [
   "art image",
   "work of visual art"
  ],
  "claims": {
   "P279": [
    "Q838948",
    "Q110910970",
    "Q2342494"
   ],
   "P1889": [
    "Q36649"
   ]
  },
  "revision_id": "2520543720",
  "ancestor_of": "Q7691687",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q17537576",
  "label": "creative work",
  "description": "artistic creation",
  "aliases": [
   "artwork",
   "work of art",
   "creative works",
   "work",
   "works"
  ],
  "claims": {
   "P31": [
    "Q133449656"
   ],
   "P279": [
    "Q15621286",
    "Q141524128"
   ],
   "P1889": [
    "Q8253",
    "Q838948",
    "Q15621286",
    "Q386724",
    "Q111955339"
   ]
  },
  "revision_id": "2568033210",
  "ancestor_of": "Q7691687",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q167035",
  "label": "project management software",
  "description": "computer software to manage projects",
  "aliases": [],
  "claims": {
   "P31": [
    "Q17155032"
   ],
   "P279": [
    "Q1391080"
   ]
  },
  "revision_id": "2483864962",
  "ancestor_of": "Q22909287",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q474157",
  "label": "collaborative software",
  "description": "application software to help people involved in a common task achieve goals",
  "aliases": [
   "groupware",
   "Collaborative software",
   "collaboration software"
  ],
  "claims": {
   "P31": [
    "Q17155032"
   ],
   "P279": [
    "Q615985"
   ]
  },
  "revision_id": "2557668904",
  "ancestor_of": "Q22909287",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1391080",
  "label": "business software",
  "description": "software program used to perform various business functions",
  "aliases": [
   "specialist application",
   "specialized application",
   "business application"
  ],
  "claims": {
   "P31": [
    "Q17155032"
   ],
   "P279": [
    "Q166142"
   ],
   "P460": [
    "Q135494458"
   ]
  },
  "revision_id": "2564315413",
  "ancestor_of": "Q22909287",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q84177695",
  "label": "to-do list manager",
  "description": "type of application software related to daily tasks management",
  "aliases": [
   "task management software",
   "to-do manager app",
   "to do list application",
   "task management application",
   "to-do apps",
   "todo utility",
   "To-do manager",
   "planning application"
  ],
  "claims": {
   "P31": [
    "Q17155032"
   ],
   "P279": [
    "Q166142"
   ],
   "P1889": [
    "Q776688"
   ]
  },
  "revision_id": "2278337122",
  "ancestor_of": "Q22909287",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q43229",
  "label": "organization",
  "description": "social entity established to meet needs or pursue goals",
  "aliases": [
   "organisation",
   "organizations",
   "organisations",
   "institution"
  ],
  "claims": {
   "P31": [
    "Q134602570",
    "Q151885",
    "Q96116695"
   ],
   "P279": [
    "Q106559804",
    "Q106668099",
    "Q1639378",
    "Q854457",
    "Q131085629"
   ],
   "P361": [
    "Q16334295",
    "Q24229398"
   ],
   "P527": [
    "Q10756188",
    "Q5",
    "Q105764136"
   ],
   "P1889": [
    "Q36993249",
    "Q2029841",
    "Q106668099",
    "Q13226383",
    "Q10387680",
    "Q40397",
    "Q141195772",
    "Q141249139"
   ]
  },
  "revision_id": "2566532090",
  "ancestor_of": "Q22909287",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q17155032",
  "label": "software category",
  "description": "metaclass of software",
  "aliases": [
   "type of software",
   "software type",
   "software categories",
   "software types",
   "types of software",
   "category of software",
   "categories of software"
  ],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q16889133",
    "Q63981612",
    "Q483394"
   ]
  },
  "revision_id": "2534148034",
  "ancestor_of": "Q22909287",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q615985",
  "label": "social software",
  "description": "type of software",
  "aliases": [],
  "claims": {
   "P31": [
    "Q17155032"
   ],
   "P279": [
    "Q3635085"
   ]
  },
  "revision_id": "2502555291",
  "ancestor_of": "Q22909287",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q166142",
  "label": "application software",
  "description": "software program or group of programs designed for end-users",
  "aliases": [
   "software application",
   "application program",
   "app",
   "computer application",
   "software",
   "application"
  ],
  "claims": {
   "P31": [
    "Q17155032"
   ],
   "P279": [
    "Q7397",
    "Q17537576"
   ],
   "P527": [
    "Q40056"
   ]
  },
  "revision_id": "2569927889",
  "ancestor_of": "Q22909287",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q134602570",
  "label": "class of being",
  "description": "collection of entities with agency defined by common characteristics",
  "aliases": [
   "kind of agent",
   "type of agent",
   "agent class",
   "agent kind",
   "agent type",
   "kind of being",
   "type of being",
   "being class",
   "being kind",
   "being type",
   "class of agent"
  ],
  "claims": {
   "P31": [
    "Q19478619",
    "Q24017414",
    "Q24017414"
   ],
   "P279": [
    "Q96251598",
    "Q134602526",
    "Q141439664"
   ],
   "P1889": [
    "Q134602505",
    "Q134602526"
   ]
  },
  "revision_id": "2568277985",
  "ancestor_of": "Q22909287",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q151885",
  "label": "concept",
  "description": "semantic unit understood in different ways, e.g. as mental representation, ability or abstract object (philosophy)",
  "aliases": [],
  "claims": {
   "P31": [
    "Q23958852"
   ],
   "P279": [
    "Q7048977",
    "Q15916540",
    "Q2145290",
    "Q1347367",
    "Q141756718"
   ],
   "P460": [
    "Q131841",
    "Q595523",
    "Q1923256",
    "Q25540110"
   ],
   "P1889": [
    "Q1969448",
    "Q595523",
    "Q17087406",
    "Q142226904"
   ]
  },
  "revision_id": "2572760103",
  "ancestor_of": "Q22909287",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q96116695",
  "label": "type of system",
  "description": "Wikidata metaclass of sets of interacting or interdependent components",
  "aliases": [
   "form of system",
   "system type",
   "system form"
  ],
  "claims": {
   "P31": [
    "Q23958852"
   ],
   "P279": [
    "Q21146257",
    "Q96251598"
   ]
  },
  "revision_id": "2553183990",
  "ancestor_of": "Q22909287",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q106559804",
  "label": "person or organization",
  "description": "class of agents",
  "aliases": [
   "person or organisation",
   "organisation or person",
   "organization or person",
   "human or organization"
  ],
  "claims": {
   "P279": [
    "Q24229398"
   ]
  },
  "revision_id": "2551510888",
  "ancestor_of": "Q22909287",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[
 {
  "synset": "oewn-01205984-n",
  "lemmas": [
   "teamwork"
  ],
  "gloss": "cooperative work done by a team (especially when it is effective)",
  "examples": [
   "it will take money, good planning and, above all, teamwork"
  ],
  "relations": {
   "hypernym": [
    "oewn-01205394-n"
   ]
  },
  "relation_targets": {
   "oewn-01205394-n": "cooperation"
  }
 }
]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 2 of 5: Service orientation (`thsmk1q1kl`)

~~~~text
Concept record:
{
 "id": "thsmk1q1kl",
 "preferred_name": "Service orientation",
 "kind": "skill",
 "broad_class": "skill",
 "variants": [
  {
   "label": "Service-Orientation"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "cex5ha398q",
  "name": "Design"
 },
 {
  "id": "gisypzf6gf",
  "name": "Communication"
 },
 {
  "id": "h4ck1veoae",
  "name": "Distributed computing"
 },
 {
  "id": "rscqfs498r",
  "name": "International Standard Book Number"
 },
 {
  "id": "fjheonyp0m",
  "name": "Monitoring"
 },
 {
  "id": "y098fizl5l",
  "name": "Object-oriented design"
 },
 {
  "id": "i0vpvmxbz0",
  "name": "Object-oriented programming"
 },
 {
  "id": "l54jfkzunm",
  "name": "Programming"
 },
 {
  "id": "qmravcc671",
  "name": "Software engineering"
 },
 {
  "id": "hctsy3pwrq",
  "name": "Spatial Orientation"
 },
 {
  "id": "crsg1gr1gz",
  "name": "Response Orientation"
 },
 {
  "id": "z4lqfruwis",
  "name": "Care coordination"
 },
 {
  "id": "n5hfz8pq8g",
  "name": "Price negotiation"
 },
 {
  "id": "k1k1pijmlc",
  "name": "Strategic prioritization"
 },
 {
  "id": "n1iikcimhd",
  "name": "Sales presentation"
 },
 {
  "id": "nb236cqujn",
  "name": "Coordination"
 },
 {
  "id": "zm7sxsrys1",
  "name": "Evidence collection"
 },
 {
  "id": "ic97ot6pm9",
  "name": "Security operations"
 },
 {
  "id": "uxc5mcnmd3",
  "name": "Executive presentations"
 },
 {
  "id": "od5cjk5y0z",
  "name": "Heavy vehicle operation"
 },
 {
  "id": "z5kqswzgmy",
  "name": "Pelvic floor rehabilitation"
 },
 {
  "id": "qlsxg8d6i9",
  "name": "Laser printing"
 },
 {
  "id": "ddfo4ab44g",
  "name": "Security Onion"
 },
 {
  "id": "atdk6aaopa",
  "name": "Big O notation"
 },
 {
  "id": "tou8ocnk8g",
  "name": "System implementation"
 },
 {
  "id": "d9otmo55ix",
  "name": "Resource mobilization"
 },
 {
  "id": "kblgtvd61c",
  "name": "Emergency vehicle operations"
 },
 {
  "id": "dcu238b2o0",
  "name": "Vehicle inspection"
 },
 {
  "id": "y3zi3hsdf6",
  "name": "IT security documentation"
 },
 {
  "id": "vb3ht42xuh",
  "name": "Service level requirement"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:2214",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Systems Administrator. …technology teams. Solid technical knowledge, as well as competencies in areas including infrastructure, data models, requirements analysis, service orientation, monitoring, understanding of enterprise, business process, and application architecture. Ability to grasp technical concepts quickly. Profi…"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[
 {
  "title": "Service-orientation",
  "revision_id": "1335212769",
  "matched_by": "title",
  "text": "Service-orientation is a design paradigm for computer software in the form of services. The principles of service-oriented design stress the separation of concerns in the software. Applying service-orientation results in units of software partitioned into discrete, autonomous, and network-accessible units, each designed to solve an individual concern. These units qualify as services.\n\nHistory of service-orientation principles and tenets\n\nService-orientation has received a lot of attention since 2003 due to the benefits it promises. These include increased return on investment, organisational agility and interoperability as well as a better alignment between business and IT. It builds heavily on earlier design paradigms and enhances them with standardisation, loose coupling and business involvement. The paradigm lost momentum in 2009; since 2014, renewed interest can be observed under the Microservices moniker. In technology, different vendor SOA platforms have used different definitions of service-orientation. Some vendors promote different principles and tenets over others, but a fair amount of commonality exists.\n\nService-orientation inherits a small number of principles from earlier paradigms including object-oriented programming, component-based software engineering and open distributed processing. It is commonly acknowledged that several service-orientation principles have their roots in the object-oriented design paradigm: the two are complementary paradigms and there will always be a need for both. Services also inherit a number of features of software components, including\n\nMultiple-use\n\nNon-context-specific\n\nComposable\n\nEncapsulated i.e., non-investigable through its interfaces\n\nA unit of independent deployment and versioning\n\nOpen Distributed Processing (ODP) combines the concepts of open systems and distributed computing, which are essential characteristics of service-orientation. The key features of ODP are all inherited by service-orientation, including federation, interoperability, heterogeneity, transparency and trading/broking.\n\nEssential characteristics\n\nDon Box was one of the first to provide a set of design guidelines referred to as his \"four tenets of service-orientation\", which he described primarily in relation to the Microsoft Indigo (subsequently Windows Communication Foundation) platform that was emerging at the time:\n\nBoundaries are explicit\n\nServices are autonomous\n\nServices share schema and contract, not class\n\nService compatibility is based on policy\n\nOther vendors and independent consultants have published their definitions of service-orientation and SOA, for instance, N. Josuttis in \"SOA in Practice\" and D: Krafzig et al. in \"Enterprise SOA\". An article in the December 2005 edition of the IBM System Journal entitled \"Impact of service orientation at the business level\" provided a study of how the service-orientation paradigm relates to fundamental componentization and the IBM Component Business Model (CBM).\n\nPaul Allen defines service orientation as a (business) paradigm, with three main components: business architecture, Service-oriented architecture and software oriented management. Allen's book defines seven Service-Oriented Viewpoints (labelled SOV7): Allen, Paul (2006). Service Orientation Winning Strategies and Best Practices. Cambridge University Press. ISBN 978-0521843362.\n\nTransparence\n\nSmoothness of customer's experience in using the service.\n\nCustomer fit\n\nAbility to tailor offerings to variations in customer needs.\n\nPartner connectivity\n\nAbility to use 3rd parties for performing commodity services\n\nAbility to offer a service to different partners\n\nAdaptation\n\nAdapting to the changes in the marketplace.\n\nMulti-channel capability\n\nSupport the customer end-to-end through process, using different channels to achieve continuity.\n\nOffering same service through different channels.\n\nOptimization\n\nOffering services in real time at high performance levels.\n\nOne-stop experience\n\nCatering to different needs of the customers through one set of services.\n\nAllen uses the viewpoints as starting point for stating questions during the design process.\n\nService-orientation has continued to receive increased recognition as an important part of the service-oriented computing landscape and a valid design approach to achieving service-oriented architecture.\n\nSee also"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q7455633",
  "label": "service-orientation",
  "description": "in business computing",
  "aliases": [],
  "claims": {},
  "revision_id": "2474833402",
  "value_labels": {},
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 3 of 5: Critical Thinking (`b9mkf081yw`)

~~~~text
Concept record:
{
 "id": "b9mkf081yw",
 "preferred_name": "Critical Thinking",
 "kind": "skill",
 "broad_class": "skill",
 "variants": [],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "gisypzf6gf",
  "name": "Communication"
 },
 {
  "id": "c6mr2nxzm3",
  "name": "Problem solving"
 },
 {
  "id": "tsdlbd9gt0",
  "name": "English"
 },
 {
  "id": "x67fsx1qco",
  "name": "Feminist theory"
 },
 {
  "id": "mdcx7ximpo",
  "name": "LESS"
 },
 {
  "id": "ss273uzint",
  "name": "Software testing"
 },
 {
  "id": "xjt0zve4ah",
  "name": "Lean principles"
 },
 {
  "id": "qayw96u2hz",
  "name": "Critical reflection"
 },
 {
  "id": "xq6qu2qcae",
  "name": "Electrical wiring"
 },
 {
  "id": "ibphs8fgxr",
  "name": "Gait training"
 },
 {
  "id": "plyin34jo8",
  "name": "Critical path method"
 },
 {
  "id": "s479attn3c",
  "name": "Surgical incision"
 },
 {
  "id": "q30r29eun4",
  "name": "Surgical suturing"
 },
 {
  "id": "k8wsre0m9r",
  "name": "Technical writing"
 },
 {
  "id": "bfd8vmdbfl",
  "name": "Athletic training"
 },
 {
  "id": "hoz7m36u58",
  "name": "Certificate in Barbering"
 },
 {
  "id": "xramob4558",
  "name": "Nutritional screening"
 },
 {
  "id": "ilwjbw0ewo",
  "name": "Criminal intelligence"
 },
 {
  "id": "jfngdt55mz",
  "name": "Experiential marketing"
 },
 {
  "id": "e23pqgx4dr",
  "name": "Education and Training"
 },
 {
  "id": "b2xq589i0g",
  "name": "Private banking"
 },
 {
  "id": "d86tb3zsu0",
  "name": "Mechanical drafting"
 },
 {
  "id": "ag7qptfyr6",
  "name": "Coastal engineering"
 },
 {
  "id": "a19c10mi46",
  "name": "Digital advertising"
 },
 {
  "id": "zu90aejpyi",
  "name": "Architectural rendering"
 },
 {
  "id": "xme4tqyrgi",
  "name": "Artificial intelligence"
 },
 {
  "id": "osw8xhiaxm",
  "name": "Nutrition care planning"
 },
 {
  "id": "r4s8o1u1q1",
  "name": "Active Listening"
 },
 {
  "id": "irydpvx389",
  "name": "Agent tool use"
 },
 {
  "id": "ai3jtul08z",
  "name": "Certified Technical Trainer"
 }
]

Usage examples from postings and syllabi:
[]

Wikipedia candidates (each with revision_id and plain text):
[
 {
  "title": "Critical thinking",
  "revision_id": "1371668361",
  "matched_by": "api-title-or-redirect",
  "text": "Critical thinking is the process of analyzing available facts, evidence, observations, and arguments to reach sound conclusions or informed choices. It involves recognizing underlying assumptions, providing justifications for ideas and actions, evaluating these justifications through comparisons with varying perspectives, and assessing their rationality and potential consequences. The goal of critical thinking is to form a judgment through the application of rational, skeptical, and unbiased analyses and evaluations. The use of the phrase critical thinking can be traced to John Dewey, who used the phrase reflective thinking, and the excellence of critical thinking in which a person can engage varies according to the individual's knowledge base on which both depend. According to philosopher Richard W. Paul, critical thinking and analysis are competencies that can be learned or trained. The application of critical thinking includes self-directed, self-disciplined, self-monitored, and self-corrective habits of the mind. Critical thinking is not a natural process; it must be induced, and ownership of the process must be taken for successful questioning and reasoning. Critical thinking presupposes a rigorous commitment to overcoming egocentrism and sociocentrism, which leads to a mindful command of effective communication and problem solving.\n\nHistory\n\nIn the classical period (5th c.–4th c. BC) of Ancient Greece, the philosopher Plato (428–347 BC) indicated that the teachings of Socrates (470–399 BC) are the earliest records of what today is called critical thinking. In an early dialogue by Plato, the philosopher Socrates debates several speakers about the ethical matter of the rightness or wrongness of Socrates escaping from prison. Upon consideration, Plato concluded that to escape prison would violate everything he believes to be greater than himself: the laws of Athens and the guiding voice that Socrates claims to hear.\n\nSocrates established the unreliability of authority and authority figures as possessors of knowledge and consequent insight; that for an individual man or woman to lead a good life that is worth living, that person must ask critical questions and possess an interrogative soul, which seeks evidence and then closely examines the available facts, and then follows the implications of the statement under analysis, thereby tracing the implications of thought and action.\n\nAs a form of co-operative argumentation, Socratic questioning requires the comparative judgment of facts, which answers then would reveal the person's irrational thinking and lack of verifiable knowledge. Socrates also demonstrated that Authority does not ensure accurate, verifiable knowledge; thus, Socratic questioning analyses beliefs, assumptions, and presumptions, by relying upon evidence and a sound rationale.\n\nIn modern times, the phrase critical thinking was coined by Pragmatist philosopher John Dewey in his book How We Think. As a type of intellectualism, the development of critical thinking is a means of critical analysis that applies rationality to develop a critique of the subject matter. According to the Foundation for Critical Thinking, in 1987 the U.S. National Council for Excellence in Critical Thinking defined critical thinking as the \"intellectually disciplined process of actively and skillfully conceptualizing, applying, analyzing, synthesizing, or evaluating information gathered from, or generated by, observation, experience, reflection, reasoning, or communication, as a guide to belief and action.\"\n\nEtymology and origin of critical thinking\n\nIn the term critical thinking, the word critical, (Grk. κριτικός = kritikos = \"critic\") derives from the word critic and implies a critique; it identifies the intellectual capacity and the means \"of judging\", \"of judgement\", \"for judging\", and of being \"able to discern\". The intellectual roots of critical thinking are as ancient as its etymology, traceable, ultimately, to the critical reasoning of the Presocractic philosophers, as well as the teaching practice and vision of Socrates 2,500 years ago who discovered by a method of probing questioning that people could not rationally justify their confident claims to knowledge.\n\nAccording to the Oxford English Dictionary, the exact term \"critical thinking\" first appeared in 1815, in the British literary journal The Critical Review, referring to critical analysis in the literary context. The meaning of \"critical thinking\" gradually evolved and expanded to mean a desirable general thinking skill by the end of the 19th century and early 20th century.\n\nDefinitions\n\nTraditionally, critical thinking has been variously defined as follows:\n\n\"The intellectually disciplined process of actively and skillfully conceptualizing, applying, analyzing, synthesizing, and/or evaluating information gathered from, or generated by, observation, experience, reflection, reasoning, or communication, as a guide to belief and action.\"\n\n\"Disciplined thinking that is clear, rational, open-minded, and informed by evidence\"\n\n\"Purposeful, self-regulatory judgment which results in interpretation, analysis, evaluation, and inference, as well as explanation of the evidential, conceptual, methodological, criteriological, or contextual considerations upon which that judgment is based\"\n\n\"Includes a commitment to using reason in the formulation of our beliefs\"\n\nThe skill and propensity to engage in an activity with reflective scepticism (McPeck, 1981)\n\nThinking about one's thinking in a manner designed to organize and clarify, raise the efficiency of, and recognize errors and biases in one's own thinking. Critical thinking is not 'hard' thinking nor is it directed at solving problems (other than 'improving' one's own thinking). Critical thinking is inward-directed with the intent of maximizing the rationality of the thinker. One does not use critical thinking to solve problems—one uses critical thinking to improve one's process of thinking.\n\n\"An appraisal based on careful analytical evaluation\"\n\n\"Critical thinking is a type of thinking pattern that requires people to be reflective, and pay attention to decision-making which guides their beliefs and actions. Critical thinking allows people to deduct with more logic, to process sophisticated information and look at various sides of an issue so they can produce more solid conclusions.\"\n\nCritical thinking has seven critical features: being inquisitive and curious, being open-minded to different sides, being able to think systematically, being analytical, being persistent to truth, being confident about critical thinking itself, and lastly, being mature.\n\nAlthough critical thinking could be defined in several different ways, there is a general agreement in its key component—the desire to reach for a satisfactory result, and this should be achieved by rational thinking and result-driven manner. Halpern thinks that critical thinking firstly involves learned abilities such as problem-solving, calculation and successful probability application. It also includes a tendency to engage the thinking process. In recent times, Stanovich believed that modern IQ testing could hardly measure the ability of critical thinking.\n\n\"Critical thinking is essentially a questioning, challenging approach to knowledge and perceived wisdom. It involves ideas and information from an objective position and then questioning this information in the light of our own values, attitudes and personal philosophy.\"\n\nContemporary critical thinking scholars have expanded these traditional definitions to include qualities, concepts, and processes such as creativity, imagination, discovery, reflection, empathy, connecting knowing, feminist theory, subjectivity, ambiguity, and inconclusiveness. Some definitions of critical thinking exclude these subjective practices.\n\nAccording to Scriven and Paul (1987), \"Critical thinking is the intellectually disciplined process of actively and skillfully conceptualizing, applying, analyzing, synthesizing, and/or evaluating information gathered from, or generated by, observation, experience, reflection, reasoning, or communication, as a guide to belief and action.\" This definition is endorsed by Harvey Siegel, Peter Facione, and Deanna Kuhn.\n\nAccording to Ennis' definition, critical thinking requires a lot of attention and brain function. When a critical thinking approach is applied to education, it helps the student's brain function better and understand texts differently.\n\nDifferent fields of study may require different types of critical thinking. Critical thinking provides more angles and perspectives upon the same material.\n\nLogic and rationality\n\nThe study of logical argumentation is relevant to the study of critical thinking. Logic is concerned with the analysis of arguments, including the appraisal of their correctness or incorrectness. In the field of epistemology, critical thinking is considered to be logically correct thinking, which allows for differentiation between logically true and logically false statements.\n\nIn \"First wave\" logical thinking, the thinker is removed from the train of thought, and the analysis of connections between concepts or points in thought is ostensibly free of any bias. In his essay Beyond Logicism in Critical Thinking Kerry S. Walters describes this ideology thus: \"A logistic approach to critical thinking conveys the message to students that thinking is legitimate only when it conforms to the procedures of informal (and, to a lesser extent, formal) logic and that the good thinker necessarily aims for styles of examination and appraisal that are analytical, abstract, universal, and objective. This model of thinking has become so entrenched in conventional academic wisdom that many educators accept it as canon\". Such principles are concomitant with the increasing dependence on a quantitative understanding of the world.\n\nIn the \"second wave\" of critical thinking, authors consciously moved away from the logocentric mode of critical thinking characteristic of the \"first wave\". Although many scholars began to take a less exclusive view of what constitutes critical thinking, rationality and logic remain widely accepted as essential bases for critical thinking. Walters argues that exclusive logicism, in the first-wave sense, is based on \"the unwarranted assumption that good thinking is reducible to logical thinking\".\n\nDeduction, abduction and induction\n\nThere are three types of logical reasoning. Informally, two kinds of logical reasoning can be distinguished in addition to formal deduction, which are induction and abduction.\n\nDeduction\n\nDeduction is the conclusion drawn from the structure of an argument's premises, by use of rules of inference formally those of propositional calculus. For example: X is human and all humans have a face, so X has a face.\nInduction\n\nInduction is drawing a conclusion from a pattern that is guaranteed by the strictness of the structure to which it applies. For example: The sum of even integers is even. Let then are even by definition. If , then , which is even; so summing two even numbers results in an even number.\nAbduction\n\nAbduction is drawing a conclusion using a heuristic that is likely, but not inevitable given some foreknowledge. For example: I observe sheep in a field, and they appear white from my viewing angle, so sheep are white. Contrast with the deductive statement: Some sheep are white on at least one side.\n\nCritical thinking and rationality\n\nKerry S. Walters, an emeritus philosophy professor from Gettysburg College, argues that rationality demands more than just logical or traditional methods of problem solving and analysis or what he calls the \"calculus of justification\" but also considers \"cognitive acts such as imagination, conceptual creativity, intuition and insight\". These \"functions\" are focused on discovery, on more abstract processes instead of linear, rules-based approaches to problem-solving. The linear and non-sequential mind must both be engaged in the rational mind.\n\nThe ability to critically analyze an argument—to dissect its structure and components, including its thesis and reasons—is essential. But so is the ability to be flexible and consider non-traditional alternatives and perspectives. These complementary functions allow critical thinking to be a practice that encompasses imagination and intuition in cooperation with traditional modes of deductive inquiry.\n\nFunctions\n\nThe list of core critical thinking skills includes observation, interpretation, analysis, inference, evaluation, explanation, and metacognition. According to Reynolds (2011), an individual or group engaged in a strong way of critical thinking gives due consideration to establish for instance:\n\nEvidence through reality\n\nContext skills to isolate the problem from context\n\nRelevant criteria for making the judgment well\n\nApplicable methods or techniques for forming the judgment\n\nApplicable theoretical constructs for understanding the problem and the question at hand\n\nIn addition to possessing strong critical-thinking skills, one must be disposed to engage problems and decisions using those skills. Critical thinking employs not only logic but broad intellectual criteria such as clarity, credibility, accuracy, precision, relevance, depth, breadth, significance, and fairness.\n\nCritical thinking calls for the ability to:\n\nRecognize problems, to find workable means for meeting those problems\n\nUnderstand the importance of prioritization and order of precedence in problem-solving\n\nGather and marshal pertinent (relevant) information\n\nRecognize unstated assumptions and values\n\nComprehend and use language with accuracy, clarity, and discernment\n\nInterpret data, to appraise evidence and evaluate arguments\n\nRecognize the existence (or non-existence) of logical relationships between propositions\n\nDraw warranted conclusions and generalizations\n\nPut to test the conclusions and generalizations at which one arrives\n\nReconstruct one's patterns of beliefs on the basis of wider experience\n\nRender accurate judgments about specific things and qualities in everyday life\n\nIn sum:\n\n\"A persistent effort to examine any belief or supposed form of knowledge in the light of the evidence that supports or refutes it and the further conclusions to which it tends.\"\n\nCritical thinking is significant in the learning process of internalization, in the construction of basic ideas, principles, and theories inherent in content. And critical thinking is significant in the learning process of application, whereby those ideas, principles, and theories are implemented effectively as they become relevant in learners' lives.\n\nIn professional fields\n\nCritical thinking is an important element of all professional fields and academic disciplines (by referencing their respective sets of permissible questions, evidence sources, criteria, etc.). It is widely recognized as an essential proficiency across professional fields and academic disciplines, where effective decision making, problem solving, and professional judgment is used. Within the framework of scientific skepticism, the process of critical thinking involves the careful acquisition and interpretation of information and use of it to reach a well-justified conclusion. The concepts and principles of critical thinking can be applied to any context or case but only by reflecting upon the nature of that application. Principles of critical thinking are broadly applicable and their usage can be seen across disciplines that each rely on its own standards such as evidence and methods. Critical thinking forms, therefore, a system of related, and overlapping, modes of thought such as anthropological thinking, sociological thinking, historical thinking, political thinking, psychological thinking, philosophical thinking, mathematical thinking, chemical thinking, biological thinking, ecological thinking, legal thinking, ethical thinking, musical thinking, thinking like a painter, sculptor, nurse, engineer, business person, etc. In other words, though critical-thinking principles are universal, their application to disciplines requires a process of reflective contextualization. Psychology offerings, for example, have included courses such as Critical Thinking about the Paranormal, in which students are subjected to a series of cold readings and tested on their belief of the \"psychic\", who is eventually announced to be a fake. In short, critical thinking is considered important for enabling a professional in any field to analyze, evaluate, explain, and restructure thinking, thereby ensuring the act of thinking without false belief.\n\nCritical thinking expands beyond the professional methods, and involves the ability to recognize bias, misinformation, and other flawed reasoning to be able to reflect on one owns reasoning. Research in cognitive psychology and professional education states that both skill development and our habitual mind or attitudes, open-mindedness and skepticism, are necessary to apply when using critical thinking.\n\nHowever, even with knowledge of the methods of logical inquiry and reasoning, mistakes occur, and due to a thinker's inability to apply the methodology consistently, and because of overruling character traits such as egocentrism. Critical thinking includes identification of prejudice, bias, propaganda, self-deception, distortion, misinformation, etc. Given research in cognitive psychology, some educators believe that schools should focus on teaching their students critical-thinking skills and cultivation of intellectual traits.\n\nHabits or traits of the mind\n\nThe habits of mind that characterize a person strongly disposed toward critical thinking include a desire to follow reason and evidence wherever they may lead, a systematic approach to problem-solving, inquisitiveness, even-handedness, and confidence in reasoning.\n\nAccording to a definition analysis by Kompf & Bond (2001), critical thinking involves problem-solving, decision making, metacognition, rationality, rational thinking, reasoning, knowledge, intelligence and also a moral component such as reflective thinking. Critical thinkers therefore need to have reached a level of maturity in their development, possess a certain attitude as well as a set of taught skills.\n\nThere is a postulation by some writers that the tendencies from habits of mind should be thought as virtues to demonstrate the characteristics of a critical thinker. These intellectual virtues are ethical qualities that encourage motivation to think in particular ways towards specific circumstances. However, these virtues have also been criticized by skeptics who argue that the evidence is lacking for a specific mental basis underpinning critical thinking.\n\nTeaching critical thinking\n\nJohn Dewey is one of many educational leaders who recognized that a curriculum aimed at building thinking skills would benefit the individual learner, the community, and democracy.\n\nIn a 2014 meta-analysis, researchers reviewed 341 quasi- or true-experimental studies of teaching critical thinking, all of which used some form of standardized critical-thinking measure. The authors describe the various methodological approaches and attempt to categorize differing assessment tools, which include standardized tests (and second-source measures), tests developed by teachers, tests developed by researchers, and tests developed by teachers who also serve the role as the researcher. The results emphasized the need for exposing students to real-world problems and the importance of encouraging open dialogue within a supportive environment. Effective strategies for teaching critical thinking are thought to be possible in a wide variety of educational settings. One attempt to assess the humanities' role in teaching critical thinking and reducing belief in pseudoscientific claims was made at North Carolina State University. Some success was noted and the researchers emphasized the value of the humanities in providing the skills to evaluate current events and qualitative data in context.\n\nHistorically, the teaching of critical thinking focused only on logical procedures such as formal and informal logic. This emphasized to students that good thinking is equivalent to logical thinking. However, a second wave of critical thinking, urges educators to value conventional techniques, meanwhile expanding what it means to be a critical thinker. In 1994, Kerry Walters compiled a conglomeration of sources surpassing this logical restriction to include many different authors' research regarding connected knowing, empathy, gender-sensitive ideals, collaboration, world views, intellectual autonomy, morality and enlightenment. These concepts invite students to incorporate their own perspectives and experiences into their thinking. \nScott Lilienfeld notes that there is some evidence to suggest that basic critical-thinking skills might be successfully taught to children at a younger age than previously thought.\n\nIn the English and Welsh school systems, Critical Thinking is offered as a subject that 16- to 18-year-olds can take as an A-Level.\n\nWell-educated citizens\n\nIn 1995, a meta-analysis of the literature on teaching effectiveness in higher education noted concerns that higher education was failing to meet society's requirements for well-educated citizens. It concluded that although faculty may aspire to develop students' thinking skills, in practice they have tended to aim at facts and concepts utilizing lowest levels of cognition, rather than developing intellect or values.\n\nCritical thinking is also considered important for human rights education for toleration. The Declaration"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q843894",
  "label": "critical thinking",
  "description": "analysis of facts, with certain levels of rigor and problem-solving abilities, to form a judgment",
  "aliases": [
   "critical reflection",
   "reflection",
   "reflection process",
   "reflective thinking"
  ],
  "claims": {
   "P31": [
    "Q15910354"
   ],
   "P279": [
    "Q1156402",
    "Q1379672"
   ],
   "P361": [
    "Q77468620",
    "Q564371"
   ]
  },
  "revision_id": "2544491167",
  "value_labels": {
   "Q15910354": "soft skills",
   "Q1156402": "reasoning",
   "Q1379672": "evaluation",
   "Q77468620": "psychological terminology",
   "Q564371": "philosophy of education"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q132145304",
  "label": "Critical Thinking",
  "description": "2025 studio album by Manic Street Preachers",
  "aliases": [],
  "claims": {
   "P31": [
    "Q482994"
   ],
   "P361": [
    "Q101160212"
   ],
   "P1889": [
    "Q66828799"
   ]
  },
  "revision_id": "2482216640",
  "value_labels": {
   "Q482994": "album",
   "Q101160212": "Manic Street Preachers' albums in chronological order",
   "Q66828799": "Critical Thinking"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q113465749",
  "label": "critical thinking",
  "description": "competency in the National Curriculum of Ghana",
  "aliases": [
   "CP"
  ],
  "claims": {
   "P31": [
    "Q1201929"
   ],
   "P361": [
    "Q113445303"
   ]
  },
  "revision_id": "2510475289",
  "value_labels": {
   "Q1201929": "core competency",
   "Q113445303": "National Curriculum of Ghana"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q15910354",
  "label": "soft skills",
  "description": "skills which are desirable in all professions",
  "aliases": [
   "common skills",
   "core skills",
   "soft skill"
  ],
  "claims": {
   "P279": [
    "Q205961"
   ]
  },
  "revision_id": "2540342691",
  "ancestor_of": "Q843894",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1156402",
  "label": "reasoning",
  "description": "type of thought and capacity of consciously making sense of things, applying logic, and adapting or justifying practices, institutions, and beliefs based on new or existing information",
  "aliases": [],
  "claims": {
   "P279": [
    "Q7048977",
    "Q9420",
    "Q1799072",
    "Q11398090"
   ]
  },
  "revision_id": "2562551290",
  "ancestor_of": "Q843894",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1379672",
  "label": "evaluation",
  "description": "determination of a subject's merit, worth, scope or significance",
  "aliases": [
   "assessment",
   "independent review",
   "quality assessment"
  ],
  "claims": {
   "P279": [
    "Q1799072",
    "Q3249551",
    "Q123304503"
   ],
   "P460": [
    "Q741332"
   ]
  },
  "revision_id": "2568301622",
  "ancestor_of": "Q843894",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q205961",
  "label": "skill",
  "description": "learned ability and competence to carry out an action",
  "aliases": [
   "athletic ability"
  ],
  "claims": {
   "P31": [
    "Q110403031"
   ],
   "P279": [
    "Q1347367",
    "Q9081"
   ],
   "P527": [
    "Q7535186",
    "Q15910354",
    "Q2480597"
   ],
   "P460": [
    "Q460693",
    "Q1813993",
    "Q7535186",
    "Q121788669"
   ],
   "P1889": [
    "Q21767554"
   ]
  },
  "revision_id": "2567571464",
  "ancestor_of": "Q843894",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q7048977",
  "label": "intangible entity",
  "description": "entity that does not have a physical existence, including abstract objects and properties",
  "aliases": [
   "abstractum",
   "non-physical entity",
   "abstract entity",
   "intangible",
   "intangible object",
   "intangible thing"
  ],
  "claims": {
   "P31": [
    "Q23958852"
   ],
   "P279": [
    "Q35120",
    "Q142208834",
    "Q142208511"
   ],
   "P361": [
    "Q18205125"
   ],
   "P1889": [
    "Q15706911",
    "Q18706315",
    "Q123139280"
   ]
  },
  "revision_id": "2572642570",
  "ancestor_of": "Q843894",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q9420",
  "label": "thought",
  "description": "mental activity involving an individual's subjective consciousness",
  "aliases": [
   "thinking skill",
   "thinking",
   "think"
  ],
  "claims": {
   "P279": [
    "Q781413"
   ],
   "P361": [
    "Q77468620",
    "Q20984829"
   ],
   "P527": [
    "Q1129066",
    "Q1123855"
   ],
   "P460": [
    "Q349047"
   ],
   "P1889": [
    "Q7784616"
   ]
  },
  "revision_id": "2572575384",
  "ancestor_of": "Q843894",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1799072",
  "label": "method",
  "description": "planned path to reaching an objective",
  "aliases": [
   "methods",
   "dul:Method"
  ],
  "claims": {
   "P31": [
    "Q1047113",
    "Q2267705"
   ],
   "P279": [
    "Q12774177",
    "Q141439861"
   ],
   "P361": [
    "Q104637332"
   ],
   "P460": [
    "Q2695280"
   ],
   "P1889": [
    "Q351682"
   ]
  },
  "revision_id": "2566702915",
  "ancestor_of": "Q843894",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q11398090",
  "label": "creation",
  "description": "intentional activity during which something comes into being and gains its characteristics",
  "aliases": [
   "creating",
   "formation",
   "forming",
   "process of forming",
   "act of forming",
   "production",
   "generation",
   "apparition",
   "making",
   "creation"
  ],
  "claims": {
   "P31": [
    "Q1914636"
   ],
   "P279": [
    "Q52948"
   ],
   "P460": [
    "Q36492844",
    "Q739302"
   ]
  },
  "revision_id": "2572666739",
  "ancestor_of": "Q843894",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q3249551",
  "label": "process",
  "description": "series of events which occur over an extended period of time",
  "aliases": [
   "bfo:Process",
   "prov:Activity",
   "event"
  ],
  "claims": {
   "P31": [
    "Q124711104",
    "Q142077035"
   ],
   "P279": [
    "Q67518978",
    "Q1190554",
    "Q141182775",
    "Q141257229"
   ],
   "P361": [
    "Q2377160",
    "Q133250"
   ],
   "P527": [
    "Q1190554",
    "Q529711",
    "Q27956567",
    "Q12769393"
   ],
   "P1889": [
    "Q24905",
    "Q224423",
    "Q3406372",
    "Q1914636",
    "Q46270982",
    "Q141609028",
    "Q141620495",
    "Q142215789"
   ]
  },
  "revision_id": "2572268752",
  "ancestor_of": "Q843894",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q123304503",
  "label": "assessment",
  "description": "process to determine qualities or characteristics of a subject",
  "aliases": [],
  "claims": {
   "P279": [
    "Q21004260"
   ]
  },
  "revision_id": "2572200384",
  "ancestor_of": "Q843894",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q482994",
  "label": "album",
  "description": "grouping of album releases by an artist usually released at the same time with the same title and tracks but in different formats for consumption (digital, CD, LP)",
  "aliases": [
   "audio album",
   "music album",
   "record album",
   "full album",
   "full-length album"
  ],
  "claims": {
   "P31": [
    "Q106043376"
   ],
   "P279": [
    "Q108346082"
   ],
   "P527": [
    "Q108352648",
    "Q141554387"
   ]
  },
  "revision_id": "2561514303",
  "ancestor_of": "Q132145304",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q106043376",
  "label": "music release type",
  "description": "Wikidata metaclass; type of music release",
  "aliases": [
   "type of music release",
   "music release form",
   "form of music release"
  ],
  "claims": {
   "P31": [
    "Q19478619",
    "Q1437361"
   ],
   "P279": [
    "Q16889133",
    "Q59913930"
   ]
  },
  "revision_id": "2547724282",
  "ancestor_of": "Q132145304",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q108346082",
  "label": "release group",
  "description": "group of similar audio releases typically of different formats (digital, CD, etc.)",
  "aliases": [
   "group of audio releases",
   "group of music releases",
   "master release"
  ],
  "claims": {
   "P279": [
    "Q16887380",
    "Q140007694"
   ],
   "P527": [
    "Q115669410"
   ]
  },
  "revision_id": "2552400352",
  "ancestor_of": "Q132145304",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1201929",
  "label": "core competency",
  "description": "concept in management theory of a harmonized combination of multiple resources and skills that distinguish a firm in the marketplace",
  "aliases": [
   "Core competence",
   "core competencies"
  ],
  "claims": {
   "P31": [
    "Q29028649"
   ],
   "P279": [
    "Q5034466",
    "Q527091",
    "Q113465652"
   ],
   "P361": [
    "Q113445303"
   ]
  },
  "revision_id": "2524177348",
  "ancestor_of": "Q113465749",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q29028649",
  "label": "economic concept",
  "description": "concept used in economic sciences",
  "aliases": [
   "economics concept",
   "concept in economics"
  ],
  "claims": {
   "P31": [
    "Q137429456"
   ],
   "P279": [
    "Q131362181"
   ],
   "P1889": [
    "Q64513524"
   ]
  },
  "revision_id": "2550617485",
  "ancestor_of": "Q113465749",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q5034466",
  "label": "capability",
  "description": "ability to execute a specified course of action",
  "aliases": [],
  "claims": {
   "P31": [
    "Q39875001"
   ],
   "P279": [
    "Q185957",
    "Q12379081"
   ],
   "P460": [
    "Q1347367"
   ],
   "P1889": [
    "Q140932463"
   ]
  },
  "revision_id": "2553024855",
  "ancestor_of": "Q113465749",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q527091",
  "label": "competence",
  "description": "ability and skill to solve problems and a willingness to do so",
  "aliases": [
   "competence (education)",
   "key competence"
  ],
  "claims": {
   "P31": [
    "Q151885"
   ],
   "P279": [
    "Q205961",
    "Q5034466"
   ]
  },
  "revision_id": "2535348068",
  "ancestor_of": "Q113465749",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q113465652",
  "label": "indicator",
  "description": "clear statements of specific things learners should know and be able to do within each content standard",
  "aliases": [],
  "claims": {
   "P279": [
    "Q113464248"
   ],
   "P361": [
    "Q113445303"
   ],
   "P527": [
    "Q1201929"
   ]
  },
  "revision_id": "2353836135",
  "ancestor_of": "Q113465749",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 4 of 5: Negotiation (`ccexfymw9t`)

~~~~text
Concept record:
{
 "id": "ccexfymw9t",
 "preferred_name": "Negotiation",
 "kind": "skill",
 "broad_class": "skill",
 "variants": [],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "mdcx7ximpo",
  "name": "LESS"
 },
 {
  "id": "c6mr2nxzm3",
  "name": "Problem solving"
 },
 {
  "id": "u9lvovjv7p",
  "name": "Creative problem-solving"
 },
 {
  "id": "jeai1j8uhz",
  "name": "French"
 },
 {
  "id": "sfx0dyxewl",
  "name": "Registered Clinical Exercise Physiologist"
 },
 {
  "id": "n5hfz8pq8g",
  "name": "Price negotiation"
 },
 {
  "id": "jh2rauw9ao",
  "name": "Memorization"
 },
 {
  "id": "vt6xft6d62",
  "name": "Demolition"
 },
 {
  "id": "t2pw81w7vy",
  "name": "Randomization"
 },
 {
  "id": "wv0l8usdcx",
  "name": "Transportation"
 },
 {
  "id": "atdk6aaopa",
  "name": "Big O notation"
 },
 {
  "id": "yzx7utgq81",
  "name": "Punctuation"
 },
 {
  "id": "f2phqfe4e5",
  "name": "Ideation"
 },
 {
  "id": "inxnx41ln3",
  "name": "Certified Perioperative Nurse (CNOR)"
 },
 {
  "id": "y83erk8o1r",
  "name": "Cost estimating"
 },
 {
  "id": "lr5nq6kgnc",
  "name": "Installation"
 },
 {
  "id": "jnssutztq4",
  "name": "Night Vision"
 },
 {
  "id": "bprelfo6pk",
  "name": "Immunization"
 },
 {
  "id": "an7k8us8vm",
  "name": "MicroStation"
 },
 {
  "id": "x4z2f6ku0u",
  "name": "Online demonstration"
 },
 {
  "id": "s95iijd8h1",
  "name": "American Osteopathic Board of Nuclear Medicine certification"
 },
 {
  "id": "rec5tl6jmm",
  "name": "Mongolian"
 },
 {
  "id": "pz26rmdqty",
  "name": "Dictation"
 },
 {
  "id": "kmodo98jyg",
  "name": "NCIDQ Certification"
 },
 {
  "id": "ez2j813g66",
  "name": "Norwegian"
 },
 {
  "id": "ewf1nb7uzl",
  "name": "Needle localization"
 },
 {
  "id": "ipfsxmf9ys",
  "name": "Content curation"
 },
 {
  "id": "jio8nmyohw",
  "name": "Refrigeration"
 },
 {
  "id": "gisypzf6gf",
  "name": "Communication"
 },
 {
  "id": "z40m891ema",
  "name": "Program optimization"
 }
]

Usage examples from postings and syllabi:
[]

Wikipedia candidates (each with revision_id and plain text):
[
 {
  "title": "Negotiation",
  "revision_id": "1374980770",
  "matched_by": "api-title-or-redirect",
  "text": "Negotiation is a dialogue between two or more parties to resolve points of difference, gain an advantage for an individual or collective, or craft outcomes to satisfy various interests. The parties aspire to agree on matters of mutual interest. The agreement can be beneficial for all or some of the parties involved. The negotiators should establish their own needs and wants while also seeking to understand the wants and needs of others involved to increase their chances of closing deals, avoiding conflicts, forming relationships with other parties, or maximizing mutual gains. Distributive negotiations, or compromises, are conducted by putting forward a position and making concessions to achieve an agreement. The degree to which the negotiating parties trust each other to implement the negotiated solution is a major factor in determining the success of a negotiation.\n\nPeople negotiate daily, often without considering it a negotiation. Negotiations may occur in organizations, including businesses, non-profits, and governments, as well as in purchasing and sales, legal proceedings, and personal situations such as marriage, divorce, parenting, friendship, etc. Professional negotiators are often specialized. Examples of professional negotiators include union negotiators, leverage buyout negotiators, peace negotiators, and hostage negotiators. They may also work under other titles, such as diplomats, legislators, or arbitrators. Negotiations may also be conducted by algorithms or machines in what is known as automated negotiation. In automated negotiation, the participants and process have to be modeled correctly. \n\nEtymology\n\nThe word \"negotiation\" originated in the early 15th century from the Old French negociacion from Latin negotiatio from neg- \"no\" and otium \"leisure\". These terms mean \"business, trade, traffic\". By the late 1570s negotiation had the definition, \"to communicate in search of mutual agreement\". With this new introduction and this meaning, it showed a shift from \"doing business\" to \"bargaining about\" business.\n\nTypes\n\nNegotiation can take a variety of forms in different contexts. These may include conferences between members of the United Nations to establish international norms, meetings between combatants to end a military conflict, meetings between representatives of businesses to bring about a transaction, and conversations between parents about how to manage childcare. Mediation is a form of negotiation where a third party helps the conflicting parties negotiate, usually when they are unable to do so by themselves. Mediated negotiation can be contrasted with arbitration, where conflicting parties commit to accepting the decision of a third party. Negotiations in the workplace can impact the entire organization's performance.\n\nNegotiation theorists generally distinguish between two primary types of negotiation: distributive negotiation and integrative negotiation. The type of negotiation that takes place is dependent on the mindset of the negotiators and the situation of the negotiation. For example, one-off encounters where lasting relationships do not occur are more likely to produce distributive negotiations whereas lasting relationships are more likely to require integrative negotiating. Theorists vary in their labeling and definition of these two fundamental types.\n\nDistributive negotiation\n\nThe total of advantages and disadvantages to be distributed in a negotiation can illustrated with the term \"negotiation pie\". The course of the negotiation can either lead to an increase, shrinking, or stagnation of these values. If the negotiating parties can expand the total pie, a win-win situation is possible, assuming that both parties profit from the expansion of the pie. In practice, however, this maximization approach is oftentimes impeded by the so-called small pie bias, i.e. the psychological underestimation of the negotiation pie's size. Likewise, the possibility to increase the pie may be underestimated due to the so-called incompatibility bias. Contrary to enlarging the pie, the pie may also shrink during negotiations e.g. due to (excessive) negotiation costs.\n\nDistributive negotiation (also known as win-lose game), compromise, positional negotiation, or hard-bargaining negotiation attempts to distribute a \"fixed pie\" of benefits. Distributive negotiation operates under zero-sum conditions, where it is assumed that any gain made by one party will be at the expense of the other. Haggling over prices on an open market, as in the purchase of a car or home, is an example of distributive negotiation.\n\nIn a distributive negotiation, each side often adopts an extreme or fixed position that they know will not be accepted, and then seeks to cede as little as possible before reaching a deal. Distributive bargainers conceive of negotiation as a process of distributing a fixed amount of value. A distributive negotiation often involves people who have never had a previous interactive relationship with each other and are unlikely to do so again shortly, although all negotiations usually have some distributive element. Since prospect theory indicates that people tend to prioritize the minimization of losses over the maximization of gains, this form of negotiation is likely to be more acrimonious and less productive in agreement.\n\nIntegrative negotiation\n\nIntegrative negotiation is also called interest-based, merit-based, win-win, or principled negotiation. It is a set of techniques that attempts to improve the quality and likelihood of negotiated agreement by taking advantage of the fact that different parties often value various outcomes differently. While distributive negotiation assumes there is a fixed amount of value (a \"fixed pie\") to be divided between the parties, integrative negotiation attempts to create value in the course of the negotiation (\"expand the pie\") by either \"compensating\" the loss of one item with gains from another (\"trade-offs\" or logrolling), or by constructing or reframing the issues of the conflict in such a way that both parties benefit (\"win-win\" negotiation).\n\nHowever, even integrative negotiation is likely to have some distributive elements, especially when the different parties value some items to the same degree or when details are left to be allocated at the end of the negotiation. While concession by at least one party is always necessary for negotiations, research shows that people who concede more quickly are less likely to explore all integrative and mutually beneficial solutions. Therefore, early concession reduces the chance of an integrative negotiation.\n\nIntegrative negotiation often involves a higher degree of trust and the formation of a relationship, although INSEAD professor Horacio Falcao has stated that, counter-intuitively, trust is a helpful aid to successful win-win negotiation but not a necessary requirement: he argues that promotion of interdependence is a more effective strategy that development of trust. Integrative negotiation can also involve creative problem-solving in the pursuit of mutual gains. It sees a good agreement as one that provides optimal gain for both parties, rather than maximum individual gain. Each party seeks to allow the other party sufficient benefit that both will hold to the agreement.\n\nProductive negotiation focuses on the underlying interests of both parties rather than their starting positions and approaches negotiation as a shared problem-solving exercise rather than an individualized battle. Adherence to objective and principled criteria is the basis for productive negotiation and agreement.\n\nText-based negotiation\n\nText-based negotiation refers to the process of working up the text of an agreement that all parties are willing to accept and sign. Negotiating parties may begin with a draft text, consider new textual suggestions, and work to find the middle ground among various differing positions.\n\nCommon examples of text-based negotiation include the redaction of a constitution, law or sentence by a constitutional assembly, legislature or court respectively. Other more specific examples are United Nations' negotiation regarding the reform of the UN Security Council and the formation of the international agreement underpinning the Regional Comprehensive Economic Partnership (RCEP) in the Asia-Pacific Region, where the parties involved failed in 2019 to agree on a text which would suit India.\n\nSuch negotiations are often founded on the principle that \"nothing is agreed until everything is agreed\". For example, this principle, also known as the single undertaking approach, is often used in World Trade Organization negotiations, although some negotiations relax this requirement. The principle formed part of the British negotiating approach for the Brexit deal following the UK's withdrawal from the European Union.\n\nIntegrated negotiation\n\nIntegrated negotiation is a strategic attempt to maximize value in any single negotiation through the astute linking and sequencing of other negotiations and decisions related to one's operating activities.\n\nThis approach in complex settings is executed by mapping out all potentially relevant negotiations, conflicts, and operating decisions to integrate helpful connections among them while minimizing any potentially harmful connections (see examples below).\n\nIntegrated negotiation is not to be confused with integrative negotiation, a different concept (as outlined above) related to a non-zero-sum approach to creating value in negotiations.\n\nIntegrated negotiation was first identified and labeled by the international negotiator and author Peter Johnston in his book Negotiating with Giants.\n\nOne of the examples cited in Johnston's book is that of J. D. Rockefeller deciding where to build his first major oil refinery. Instead of taking the easier, cheaper route from the oil fields to refine his petroleum in Pittsburgh, Rockefeller chose to build his refinery in Cleveland, because he recognized that he would have to negotiate with the rail companies transporting his refined oil to market. Pittsburgh had just one major railroad, which would therefore be able to dictate prices in negotiations, while Cleveland had three railroads that Rockefeller knew would compete for his business, potentially reducing his costs significantly. The leverage gained in these rail negotiations more than offset the additional operating costs of sending his oil to Cleveland for refining, helping establish Rockefeller's empire, while undermining his competitors who failed to integrate their core operating decisions with their negotiation strategies.\n\nOther examples of integrated negotiation include the following:\n\nIn sports, athletes in the final year of their contracts will ideally hit peak performance so they can negotiate robust, long-term contracts in their favor.\n\nA union needs to negotiate and resolve any significant internal conflicts to maximize its collective clout before going to the table to negotiate a new contract with management.\n\nIf purchases for similar goods or services are occurring independently of one another across different government departments, recognizing this and consolidating orders into one large volume purchase can help create buying leverage and cost savings in negotiations with suppliers.\n\nA tech start-up looking to negotiate being bought out by a larger industry player in the future can improve its odds of that happening by ensuring, wherever possible, that its systems, technology, competencies, and culture are as compatible as possible with those of its most likely buyer.\n\nA politician negotiating support for a presidential run may want to avoid bringing on board any high-profile supporters who risk alienating other important potential supporters while avoiding any unexpected new policies that could also limit the size of their growing coalition.\n\nSole source negotiation\n\nSole source negotiation arises when a buyer has no apparent alternatives but to purchase from a specific supplier or attempt to secure a better deal without any alternative.\n\nBad faith\n\nWhen a party pretends to negotiate but secretly has no intention of compromising, the party is negotiating in bad faith; for example, when a political party sees political benefit in appearing to negotiate without having any intention of making the compromises necessary to settle.\n\nBad faith negotiations are often used in political science and political psychology to refer to negotiating strategies in which there is no real intention to reach compromise or a model of information processing. The \"inherent bad faith model\" of information processing is a theory in political psychology that was first put forth by Ole Holsti to explain the relationship between John Foster Dulles' beliefs and his model of information processing. It is the most widely studied model of one's opponent. A state is presumed implacably hostile, and contra-indicators of this are ignored. They are dismissed as propaganda ploys or signs of weakness. An example is John Foster Dulles' position regarding the Soviet Union.\n\nInternational negotiation\n\nDue to different cultural lenses, negotiation styles differ worldwide. These differences comprise among others how the parties exchange information, the use of different strategies, conceptions of the nature of negotiation, the use of power, the use of options. Negotiations as they are often taught and used by practitioners in \"Western\" countries may not be effective or may even be counterproductive in \"non-Western\" countries – such as Asian countries. These cultural differences can lead to misunderstandings, misinterpretations, and conflicts that hinder effective deal-making. Overcoming these barriers requires cultural awareness, adaptability, and strategic communication.\n\nStrategies\n\nThere are many different ways to categorize the essential elements of negotiation.\n\nOne view of negotiation involves three basic elements: process, behavior, and substance. The process refers to how the parties negotiate: the context of the negotiations, the parties to the negotiations, the tactics used by the parties, and the sequence and stages in which all of these play out. Behavior refers to the relationships among these parties, the communication between them, and the styles they adopt. The substance refers to what the parties negotiate over: the agenda, the issues (positions and – more helpfully – interests), the options, and the agreement(s) reached at the end.\n\nAnother view of negotiation comprises four elements: strategy, process, tools, and tactics. The strategy comprises top-level goals, which typically include the relationship and the intended outcome. Processes and tools include the steps to follow and roles to take in preparing for and negotiating with the other parties. Tactics include more detailed statements and actions and responses to others' statements and actions. Some add to this persuasion and influence, asserting that these have become integral to modern-day negotiation success, and so should not be omitted.\n\nStrategic approaches to concession-making include consideration of the optimum time to make a concession, making concessions in installments, not all at once, and ensuring that the opponent is aware that a concession has been made, rather than a re-expression of a position already outlined, and aware of the cost incurred in making the concession, especially where the other party is generally less aware of the nature of the business or the product being negotiated.\n\nStages in the negotiation process\n\nEffective negotiation begins with planning and collating any necessary information. One aspect of planning is the development of a \"best alternative to a negotiated agreement\", or BATNA: the most advantageous alternative course of action that a negotiator can take, should the current negotiation end without reaching an agreement. Anticipating the possibility of being unsuccessful is therefore important. The quality of a BATNA has the potential to improve a party's negotiation outcome. Understanding one's BATNA can empower an individual and allow him or her to set higher goals when moving forward. Alternatives need to be actual and actionable to be of value. Negotiators may also consider the other party's BATNA and how it compares to what they are offering during the negotiation.\n\nNegotiators do not need to sacrifice effective negotiation in favor of a positive relationship between parties. Rather than conceding, each side can appreciate that the other has emotions and motivations of their own and use this to their advantage in discussing the issue. Understanding perspectives can help move parties toward a more integrative solution. Fisher et al. illustrate a few techniques that effectively improve perspective-taking in the book Getting to Yes, and through the following, negotiators can separate people from the problem itself:\n\nPut yourself in their shoes – People tend to search for information that confirms their own beliefs and often ignore information that contradicts prior beliefs. To negotiate effectively, it is important to empathize with the other party's point of view. One should be open to other views and attempt to approach an issue from the perspective of the other.\n\nDiscuss each other's perceptions – A more direct approach to understanding the other party is to explicitly discuss each other's perceptions. Each individual should openly and honestly share their perceptions without assigning blame or judgment to the other.\n\nFind opportunities to act inconsistently with their views – The other party may have prior perceptions and expectations about the other side. The other side can act in a way that directly contradicts those preconceptions, effectively conveying that the party is interested in an integrative negotiation.\n\nFace-saving – This approach justifies a stance based on one's previously expressed principles and values in a negotiation. This approach to an issue is less arbitrary, and thus, it is more understandable from the opposing party's perspective.\n\nAdditionally, negotiators can use specific communication techniques to build stronger relationships and develop more meaningful negotiation solutions.\n\nActive listening – Listening is more than just hearing what the other side says. Active listening involves paying close attention to what is being said verbally and nonverbally. It involves periodically seeking further clarification from the person. By asking the person exactly what they mean, they may realize the negotiator takes them seriously and is not simply walking through a routine. The Australian Mosaic Project Services business commends \"proactive\" rather than just \"active\" listening, in which more emphasis is placed on the asking of questions as well as listening actively to the answers given.\n\nSpeak for a purpose – Too much information can be as harmful as too little. Before discussing an important point, determine exactly what to communicate to the other party. Determine the exact purpose that this shared information will serve.\n\nEmploying an advocate\n\nA skilled negotiator may serve as an advocate for one party to the negotiation. The advocate attempts to obtain the most favorable outcomes possible for that party. In this process, the negotiator attempts to determine the minimum outcome(s) the other party is (or parties are) willing to accept, then adjusts their demands accordingly. A \"successful\" negotiation in the advocacy approach is when the negotiator can obtain all or most of the outcomes their party desires, but without driving the other party to permanently break off negotiations.\n\nSkilled negotiators may use a variety of tactics ranging from negotiation hypnosis to a straightforward presentation of demands or setting of preconditions, to more deceptive approaches such as cherry picking. Intimidation and salami tactics may also play a part in swaying the outcome of negotiations.\n\nConsistency\n\nIn negotiation, consistency refers to a negotiator's strong psychological need to be consistent with prior acts and statements. The consistency principle states that people are motivated toward cognitive consistency and will change their attitudes, beliefs, perceptions and actions to achieve it. Robert Cialdini and his research team have conducted extensive research into what Cialdini refers to as the 'Consistency Principle of Persuasion'. Described in his book Influence Science and Practice, this principle states that people live up to what they have publicly said they will do and what they have written down. Cialdini"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q202875",
  "label": "negotiation",
  "description": "dialogue between two or more people or parties intended to reach a beneficial outcome",
  "aliases": [
   "negotiating"
  ],
  "claims": {
   "P279": [
    "Q131395",
    "Q1914636",
    "Q1456892"
   ],
   "P1889": [
    "Q11790475"
   ]
  },
  "revision_id": "2567568475",
  "value_labels": {
   "Q131395": "dialogue",
   "Q1914636": "activity",
   "Q1456892": "peace process",
   "Q11790475": ""
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q114507716",
  "label": "Negotiation",
  "description": "episode of NewsRadio (S2 E8)",
  "aliases": [],
  "claims": {
   "P31": [
    "Q21191270"
   ]
  },
  "revision_id": "2540669263",
  "value_labels": {
   "Q21191270": "television series episode"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q131395",
  "label": "dialogue",
  "description": "conversation between two or more people",
  "aliases": [
   "dialog"
  ],
  "claims": {
   "P31": [
    "Q41172303",
    "Q1406161",
    "Q223393"
   ],
   "P279": [
    "Q17584038",
    "Q3685487"
   ],
   "P460": [
    "Q3030248",
    "Q52943"
   ],
   "P1889": [
    "Q3025978"
   ]
  },
  "revision_id": "2567636314",
  "ancestor_of": "Q202875",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1914636",
  "label": "activity",
  "description": "series of actions done by an agent which results in an external change of state",
  "aliases": [
   "act",
   "action",
   "operation",
   "doing",
   "do",
   "acting",
   "practice",
   "db:Process",
   "dol:Process",
   "dul:Process",
   "gfo:Process"
  ],
  "claims": {
   "P31": [
    "Q116505632"
   ],
   "P279": [
    "Q3249551",
    "Q141187917",
    "Q141222018"
   ],
   "P527": [
    "Q4026292",
    "Q52948",
    "Q24902509"
   ],
   "P460": [
    "Q1656682"
   ],
   "P1889": [
    "Q4026292",
    "Q12737077",
    "Q192581",
    "Q3249551",
    "Q142215789"
   ]
  },
  "revision_id": "2572268874",
  "ancestor_of": "Q202875",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1456892",
  "label": "peace process",
  "description": "ensemble of negotiations, agreements and actions to resolve an armed conflict",
  "aliases": [],
  "claims": {
   "P279": [
    "Q1194317",
    "Q11827330"
   ],
   "P1889": [
    "Q134082181"
   ]
  },
  "revision_id": "2537557124",
  "ancestor_of": "Q202875",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q41172303",
  "label": "core concept",
  "description": "main aspect of a topic",
  "aliases": [],
  "claims": {
   "P31": [
    "Q137429456"
   ],
   "P279": [
    "Q151885"
   ]
  },
  "revision_id": "2443479953",
  "ancestor_of": "Q202875",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1406161",
  "label": "artistic theme",
  "description": "theme or subject in a work of art",
  "aliases": [
   "theme",
   "artistic subject",
   "painting theme",
   "painting subject",
   "art theme",
   "Aihe",
   "motif",
   "artistic motif",
   "art motif"
  ],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q20742825",
    "Q123139280"
   ],
   "P460": [
    "Q1053916",
    "Q42109240",
    "Q2995443"
   ]
  },
  "revision_id": "2567848366",
  "ancestor_of": "Q202875",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q223393",
  "label": "literary genre",
  "description": "category of literary composition",
  "aliases": [
   "book genre",
   "writing genre",
   "literature genre"
  ],
  "claims": {
   "P31": [
    "Q140354262",
    "Q109551565"
   ],
   "P279": [
    "Q1792379"
   ],
   "P361": [
    "Q116518880"
   ],
   "P527": [
    "Q12104030",
    "Q12119802"
   ],
   "P1889": [
    "Q4263830",
    "Q621993",
    "Q11796169",
    "Q1194480",
    "Q109598321",
    "Q110169000",
    "Q117422294"
   ]
  },
  "revision_id": "2563793113",
  "ancestor_of": "Q202875",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q17584038",
  "label": "oral media",
  "description": "",
  "aliases": [],
  "claims": {
   "P279": [
    "Q340169"
   ]
  },
  "revision_id": "2527572613",
  "ancestor_of": "Q202875",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q116505632",
  "label": "type of process",
  "description": "Wikidata metaclass of process",
  "aliases": [
   "process type"
  ],
  "claims": {
   "P31": [
    "Q19478619",
    "Q24017414"
   ],
   "P279": [
    "Q142077035"
   ],
   "P361": [
    "Q58778"
   ],
   "P1889": [
    "Q138611570"
   ]
  },
  "revision_id": "2566753342",
  "ancestor_of": "Q202875",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q3249551",
  "label": "process",
  "description": "series of events which occur over an extended period of time",
  "aliases": [
   "bfo:Process",
   "prov:Activity",
   "event"
  ],
  "claims": {
   "P31": [
    "Q124711104",
    "Q142077035"
   ],
   "P279": [
    "Q67518978",
    "Q1190554",
    "Q141182775",
    "Q141257229"
   ],
   "P361": [
    "Q2377160",
    "Q133250"
   ],
   "P527": [
    "Q1190554",
    "Q529711",
    "Q27956567",
    "Q12769393"
   ],
   "P1889": [
    "Q24905",
    "Q224423",
    "Q3406372",
    "Q1914636",
    "Q46270982",
    "Q141609028",
    "Q141620495",
    "Q142215789"
   ]
  },
  "revision_id": "2572268752",
  "ancestor_of": "Q202875",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q141187917",
  "label": "stative",
  "description": "perdurant that when summed to another perdurant of the same type, gives a perdurant of the same type",
  "aliases": [
   "cumulative perdurant"
  ],
  "claims": {
   "P31": [
    "Q142077035"
   ],
   "P279": [
    "Q141257229",
    "Q141204674"
   ]
  },
  "revision_id": "2571203743",
  "ancestor_of": "Q202875",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q141222018",
  "label": "occurrent (GFO)",
  "description": "GFO class",
  "aliases": [
   "gfo:Occurrent",
   "occurrent"
  ],
  "claims": {
   "P279": [
    "Q141183644"
   ],
   "P1889": [
    "Q67518978",
    "Q141204674"
   ]
  },
  "revision_id": "2561058205",
  "ancestor_of": "Q202875",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1194317",
  "label": "conflict resolution",
  "description": "methods and processes involved in facilitating the peaceful ending of conflict and retribution",
  "aliases": [
   "reconciliation",
   "conflict settlement",
   "settlement of conflicts",
   "conflict management"
  ],
  "claims": {
   "P31": [
    "Q11862829",
    "Q131744452"
   ],
   "P279": [
    "Q11024",
    "Q730920"
   ],
   "P361": [
    "Q55659895"
   ],
   "P1889": [
    "Q1781444"
   ]
  },
  "revision_id": "2549404403",
  "ancestor_of": "Q202875",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q11827330",
  "label": "political process",
  "description": "type of process",
  "aliases": [],
  "claims": {
   "P31": [
    "Q116505632"
   ],
   "P279": [
    "Q2305441"
   ]
  },
  "revision_id": "2551853859",
  "ancestor_of": "Q202875",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q21191270",
  "label": "television series episode",
  "description": "single installment of a television series",
  "aliases": [
   "television episode",
   "TV episode",
   "TV series episode",
   "TV show episode",
   "television show episode"
  ],
  "claims": {
   "P279": [
    "Q1983062",
    "Q2431196",
    "Q15416"
   ],
   "P361": [
    "Q5398426",
    "Q3464665",
    "Q1259759"
   ],
   "P1889": [
    "Q1983062",
    "Q29555881",
    "Q21664088",
    "Q50062923",
    "Q1464125",
    "Q50914552",
    "Q99079902",
    "Q106942341"
   ]
  },
  "revision_id": "2553201552",
  "ancestor_of": "Q114507716",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1983062",
  "label": "episode",
  "description": "part of a work such as a serial television or radio drama",
  "aliases": [
   "radio episode",
   "episodes"
  ],
  "claims": {
   "P279": [
    "Q11578774"
   ],
   "P361": [
    "Q15709880",
    "Q526877",
    "Q136147086"
   ],
   "P1889": [
    "Q21191270",
    "Q1980247",
    "Q3925766",
    "Q1347347"
   ]
  },
  "revision_id": "2569946872",
  "ancestor_of": "Q114507716",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q2431196",
  "label": "audiovisual work",
  "description": "creative work possessing both a sound and a visual component",
  "aliases": [
   "audial visual work",
   "audial visual works",
   "audial-visual work",
   "audial-visual works",
   "work (audio visual)",
   "work (audio-visual)",
   "work (audiovisual)",
   "works (audio visual)",
   "works (audio-visual)",
   "works (audiovisual)",
   "audio visual work"
  ],
  "claims": {
   "P279": [
    "Q17537576",
    "Q194980",
    "Q106213450",
    "Q110879282",
    "Q110910970"
   ],
   "P1889": [
    "Q10301427",
    "Q114797752"
   ]
  },
  "revision_id": "2515922050",
  "ancestor_of": "Q114507716",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q15416",
  "label": "television program",
  "description": "segment of audiovisual content intended for broadcast and streaming on television",
  "aliases": [
   "television programme",
   "television show",
   "TV program",
   "TV show",
   "TV programme",
   "TV broadcast",
   "television broadcast",
   "T.V. program",
   "T. V. program",
   "T.V. show",
   "T. V. show",
   "T.V. broadcast",
   "T. V. broadcast",
   "television appearance",
   "streaming television"
  ],
  "claims": {
   "P31": [
    "Q110562117"
   ],
   "P279": [
    "Q11578774",
    "Q2431196",
    "Q10301427",
    "Q7725310"
   ],
   "P361": [
    "Q12376699",
    "Q289"
   ],
   "P1889": [
    "Q1407245",
    "Q1555508"
   ]
  },
  "revision_id": "2570981425",
  "ancestor_of": "Q114507716",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[
 {
  "synset": "oewn-07162900-n",
  "lemmas": [
   "negotiation",
   "dialogue",
   "talks"
  ],
  "gloss": "a discussion intended to produce an agreement",
  "examples": [
   "the buyout negotiation lasted several days",
   "they disagreed but kept an open dialogue",
   "talks between Israelis and Palestinians"
  ],
  "relations": {
   "hypernym": [
    "oewn-07155367-n"
   ],
   "hyponym": [
    "oewn-07156145-n",
    "oewn-07163281-n",
    "oewn-07164544-n",
    "oewn-07164731-n",
    "oewn-07165207-n",
    "oewn-07165352-n"
   ]
  },
  "relation_targets": {
   "oewn-07155367-n": "discussion, give-and-take, word",
   "oewn-07156145-n": "parley",
   "oewn-07163281-n": "diplomacy, diplomatic negotiations",
   "oewn-07164544-n": "bargaining",
   "oewn-07164731-n": "collective bargaining",
   "oewn-07165207-n": "horse trading",
   "oewn-07165352-n": "mediation"
  }
 },
 {
  "synset": "oewn-01268857-n",
  "lemmas": [
   "negotiation"
  ],
  "gloss": "the activity or business of negotiating an agreement; coming to terms",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-00408356-n"
   ]
  },
  "relation_targets": {
   "oewn-00408356-n": "activity"
  }
 }
]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 5 of 5: Attention to detail (`gdzh66chlx`)

~~~~text
Concept record:
{
 "id": "gdzh66chlx",
 "preferred_name": "Attention to detail",
 "kind": "ability",
 "broad_class": "ability",
 "variants": [
  {
   "label": "Detail Conscious"
  },
  {
   "label": "Detail oriented"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "tsdlbd9gt0",
  "name": "English"
 },
 {
  "id": "gisypzf6gf",
  "name": "Communication"
 },
 {
  "id": "b9mkf081yw",
  "name": "Critical Thinking"
 },
 {
  "id": "rdtwc1bnps",
  "name": "Speaking"
 },
 {
  "id": "f69xny35zm",
  "name": "SQL"
 },
 {
  "id": "g32rgj6uc5",
  "name": "Goal-oriented"
 },
 {
  "id": "crm3w31oq7",
  "name": "Team-oriented"
 },
 {
  "id": "cd19a0euqf",
  "name": "Residential construction"
 },
 {
  "id": "id244h1e6v",
  "name": "Results-oriented"
 },
 {
  "id": "vlx37w32ol",
  "name": "Email on Acid"
 },
 {
  "id": "z3d8t5kt64",
  "name": "OrientDB"
 },
 {
  "id": "cezarn1svy",
  "name": "Automotive detailing"
 },
 {
  "id": "jnut7g5uci",
  "name": "Email etiquette"
 },
 {
  "id": "c0kd1bmd4t",
  "name": "Dental records"
 },
 {
  "id": "kpy86mibqf",
  "name": "Taxi license"
 },
 {
  "id": "iz17ednjvl",
  "name": "Digital currencies"
 },
 {
  "id": "hctsy3pwrq",
  "name": "Spatial Orientation"
 },
 {
  "id": "xl6126omq1",
  "name": "Dairy science"
 },
 {
  "id": "myqo7j7o11",
  "name": "Label printer"
 },
 {
  "id": "bt632lzc9o",
  "name": "Design consultation"
 },
 {
  "id": "leu6zjs1w7",
  "name": "Traffic collision reconstruction"
 },
 {
  "id": "gov0d8zbms",
  "name": "Resilience"
 },
 {
  "id": "w1fhvynkfa",
  "name": "Associate of Applied Science in Dental Hygiene"
 },
 {
  "id": "kokxhnhui7",
  "name": "Design of experiments"
 },
 {
  "id": "u4n357y1ti",
  "name": "Animal science"
 },
 {
  "id": "ihcdms58ev",
  "name": "Email software"
 },
 {
  "id": "pts4mjn76g",
  "name": "Financial consolidation"
 },
 {
  "id": "znkj1vnxbh",
  "name": "Data center design"
 },
 {
  "id": "oia7a9p9lz",
  "name": "Behavioural science"
 },
 {
  "id": "l39uixm3x0",
  "name": "Bridal consulting"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "scrapifier/indeed-usa-job-postings@v1/indeed_usa_job_postings.csv:3",
  "source": "kaggle:scrapifier/indeed-usa-job-postings (CC0: Public Domain), column description",
  "text": "Job title: Morning Bartender. … Bartender, you will be the first face our guests see, setting the tone for an exceptional dining and drinking experience. Your enthusiasm, attention to detail, and expertise in beverage service will create a welcoming atmosphere that keeps guests coming back. This role offers a fantastic opportunit…"
 },
 {
  "id": "mohityd2007/real-world-job-postings-dataset-for-ml-projects@v1/jobs_data.csv:28",
  "source": "kaggle:mohityd2007/real-world-job-postings-dataset-for-ml-projects (Attribution 4.0 International (CC BY 4.0)), column Job Description",
  "text": "Job title: Human Resources (HR) Associate. MS-Office,MS-Word,Attention to Detail,MS-Excel,English Proficiency (Spoken),English Proficiency (Written),Document Management,"
 },
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:305",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Business Analyst. …gnostics results to clearly articulate business opportunities Configure model with limited mentorship from project lead Demonstrates superb attention to detail Demonstrates interest and/or competence in tools needed to deliver project analysis (Excel, Power Pivot, and other analytical tools and soft…"
 },
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:1040",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: Reverse Data Analyst. [\"Data Analysis\", \"Excel\", \"SQL\", \"BI Tools\", \"Attention To Detail\"]"
 },
 {
  "id": "priyankamalavade/naukri-jobs-details@v1/naukri_data_analyst_jobs.csv:131",
  "source": "kaggle:priyankamalavade/naukri-jobs-details (MIT), column Description",
  "text": "Job title: Research Analyst. Critical Thinking, Strategic Thinking, Attention To Detail, Decision Making, Communication Skills, Presentation Skills, Analytical, Public Speaking"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[
 {
  "title": "Attention to Detail",
  "revision_id": "1362726597",
  "matched_by": "title",
  "text": "Attention to Detail Ltd (ATD) was a British video game developer based in Hatton. Founded by University of Birmingham graduates in September 1988, it was acquired by Kaboom Studios in January 1997. They were known for developing the Rollcage series. The studio shut down in August 2003 due to financial issues at Kaboom Studios.\n\nHistory\n\nIn mid-1987, Chris Gibbs, Martin Green, Nalin Sharma, and Jon Steele created the Atari ST port of Super Sprint for Activision. Sharma had already had experience developing Commodore 64 and contacts in the video game industry, which enabled the group's partnership with Activision. The conversion was finished in twelve weeks. Simultaneously, Fred Gill had developed the game Octan for the ZX Spectrum, which he sold to Firebird. Gibbs, Gill, Green, and Stelle, as well as Jim Torjussen, founded Attention to Detail in September 1988. All founders were University of Birmingham graduates. The company occupied 12,000 square feet (1,100 m) of converted barns in Hatton, in rural Warwickshire. In January 1997, the company was acquired by Geoff Brown, who established Geoff Brown Holdings (later Kaboom Studios) to manage the ownership. Amid financial struggles at Kaboom Studios and with Attention to Detail unable to find a publisher for Ion Runner, the studio was placed into liquidation on 28 August 2003, laying off all 50 staff members and cancelling Ion Runner.\n\nGames developed\n\nReferences"
 },
 {
  "title": "Attention to Detail (album)",
  "revision_id": "1345835298",
  "matched_by": "title-minus-qualifier",
  "text": "Attention to Detail is the second solo studio album by Nigerian singer Kcee. It was released on 24 August 2017 by Five Star Music and features guest appearances from Falz, 2Baba, Tekno, Flavour, Olamide, Patoranking, Phyno, Shatta Wale, and Sauti Sol. Its production was mainly handled by Mystro, along with additional production from Blaq Jerzee, Dr Amir, and Krizbeatz. The album serves as a follow-up to Kcee's debut, Take Over (2013).\n\nBackground and promotion\n\nIn the lead-up to Attention to Detail, Kcee revealed his intention to combine his music career with political aspirations. In August 2017, he announced plans to run for the office of the governor of Anambra State ahead of Nigeria's 2019 general elections. The album was positioned as part of this new chapter, with Kcee encouraging young people and his fan base to get involved in national development. \"I encourage every youth and all of my fans to join this movement of contributing our quota to the rescue of this great nation,\" he wrote on Instagram. Kcee revealed the tracklist for Attention to Detail three days before the album's release.\n\nSingles\n\nThe album's lead single, \"Tender\", featuring Tekno, was released on 12 October 2016. It is one of the album's bonus tracks. The music video for \"Tender\" was released on 23 November 2016 and directed by Patrick Elis. Another one of the album's bonus tracks, \"Romantic Call\", was released on 9 March 2017 as the album's second single. The accompanying music video was directed by Director Ace and Zacky Madar. \"Desire\", another bonus track off the album was released as Attention to Detail's third single on 18 April 2017. The Mystro-produced \"We Go Party\" featuring Olamide was released as the album's fourth single. The Owanbe-themed music video for \"We Go Party\" was directed by Unlimited L.A and featured cameos from the likes of DJ Jimmy Jatt and Iyabo Ojo. The album's fifth single \"Vanessa\" was released on 9 August 2017, alongside its music video. \"Vanessa\" was produced by Mystro. The sixth single \"Dance\" featuring Phyno was released on 13 September 2017; its music video was directed by Clarence Peters. The seventh and final single \"Whine for Me\" features Kenyan afropop band Sauti Sol and was released on 26 October 2017, alongside its music video.\n\nCritical reception\n\nJoey Akan of Pulse Nigeria rated Attention to Detail a 3.5/5, describing it as an ambitious but largely one-dimensional pop project driven by Kcee's usual flair for mass appeal and grandiosity. While the album showed moments of experimentation, it mostly stuck to contemporary highlife and feel-good anthems, with Akan concluding, “To his credit, Kcee shows ambition and experimentation on “Attention To Detail,\" but it is his insistence on contemporary highlife that dominates this project.” Wilfred Okiche of 360nobs described Attention to Detail as a predictable but occasionally enjoyable project that played to Kcee's strengths: catchy, disposable pop songs with danceable highlife influences. Despite a few pleasant moments, Okiche concluded, “Some more attention to detail and Kcee could have had a contained record. This one doesn’t live up to the title.”\n\nTrack listing\n\nRelease history\n\nReferences"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q2870052",
  "label": "Attention to Detail",
  "description": "British video game developer",
  "aliases": [
   "Attention to Detail Limited"
  ],
  "claims": {
   "P31": [
    "Q210167"
   ]
  },
  "revision_id": "2552568196",
  "value_labels": {
   "Q210167": "video game developer"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q136032032",
  "label": "Attention to Detail",
  "description": "2017 album by Kcee",
  "aliases": [],
  "claims": {
   "P31": [
    "Q482994"
   ]
  },
  "revision_id": "2461666086",
  "value_labels": {
   "Q482994": "album"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q137161161",
  "label": "Attention to Detail",
  "description": "episode of Santa Clarita Diet (S1 E6)",
  "aliases": [],
  "claims": {
   "P31": [
    "Q21191270"
   ]
  },
  "revision_id": "2566909724",
  "value_labels": {
   "Q21191270": "television series episode"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q210167",
  "label": "video game developer",
  "description": "software development organization specializing in the creation of video games (for person use Q58287519)",
  "aliases": [
   "game studio",
   "video game development studio",
   "video game studio",
   "video game development company",
   "game development studio",
   "game development company",
   "videogame development studio",
   "software studio"
  ],
  "claims": {
   "P279": [
    "Q112042224",
    "Q43229"
   ],
   "P1889": [
    "Q58287519",
    "Q1137109"
   ]
  },
  "revision_id": "2561507649",
  "ancestor_of": "Q2870052",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q112042224",
  "label": "video game company",
  "description": "company working in the video game industry",
  "aliases": [
   "software studio"
  ],
  "claims": {
   "P279": [
    "Q1058914"
   ],
   "P527": [
    "Q210167",
    "Q1137109"
   ]
  },
  "revision_id": "2565685746",
  "ancestor_of": "Q2870052",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q43229",
  "label": "organization",
  "description": "social entity established to meet needs or pursue goals",
  "aliases": [
   "organisation",
   "organizations",
   "organisations",
   "institution"
  ],
  "claims": {
   "P31": [
    "Q134602570",
    "Q151885",
    "Q96116695"
   ],
   "P279": [
    "Q106559804",
    "Q106668099",
    "Q1639378",
    "Q854457",
    "Q131085629"
   ],
   "P361": [
    "Q16334295",
    "Q24229398"
   ],
   "P527": [
    "Q10756188",
    "Q5",
    "Q105764136"
   ],
   "P1889": [
    "Q36993249",
    "Q2029841",
    "Q106668099",
    "Q13226383",
    "Q10387680",
    "Q40397",
    "Q141195772",
    "Q141249139"
   ]
  },
  "revision_id": "2566532090",
  "ancestor_of": "Q2870052",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q482994",
  "label": "album",
  "description": "grouping of album releases by an artist usually released at the same time with the same title and tracks but in different formats for consumption (digital, CD, LP)",
  "aliases": [
   "audio album",
   "music album",
   "record album",
   "full album",
   "full-length album"
  ],
  "claims": {
   "P31": [
    "Q106043376"
   ],
   "P279": [
    "Q108346082"
   ],
   "P527": [
    "Q108352648",
    "Q141554387"
   ]
  },
  "revision_id": "2561514303",
  "ancestor_of": "Q136032032",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q106043376",
  "label": "music release type",
  "description": "Wikidata metaclass; type of music release",
  "aliases": [
   "type of music release",
   "music release form",
   "form of music release"
  ],
  "claims": {
   "P31": [
    "Q19478619",
    "Q1437361"
   ],
   "P279": [
    "Q16889133",
    "Q59913930"
   ]
  },
  "revision_id": "2547724282",
  "ancestor_of": "Q136032032",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q108346082",
  "label": "release group",
  "description": "group of similar audio releases typically of different formats (digital, CD, etc.)",
  "aliases": [
   "group of audio releases",
   "group of music releases",
   "master release"
  ],
  "claims": {
   "P279": [
    "Q16887380",
    "Q140007694"
   ],
   "P527": [
    "Q115669410"
   ]
  },
  "revision_id": "2552400352",
  "ancestor_of": "Q136032032",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q21191270",
  "label": "television series episode",
  "description": "single installment of a television series",
  "aliases": [
   "television episode",
   "TV episode",
   "TV series episode",
   "TV show episode",
   "television show episode"
  ],
  "claims": {
   "P279": [
    "Q1983062",
    "Q2431196",
    "Q15416"
   ],
   "P361": [
    "Q5398426",
    "Q3464665",
    "Q1259759"
   ],
   "P1889": [
    "Q1983062",
    "Q29555881",
    "Q21664088",
    "Q50062923",
    "Q1464125",
    "Q50914552",
    "Q99079902",
    "Q106942341"
   ]
  },
  "revision_id": "2553201552",
  "ancestor_of": "Q137161161",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1983062",
  "label": "episode",
  "description": "part of a work such as a serial television or radio drama",
  "aliases": [
   "radio episode",
   "episodes"
  ],
  "claims": {
   "P279": [
    "Q11578774"
   ],
   "P361": [
    "Q15709880",
    "Q526877",
    "Q136147086"
   ],
   "P1889": [
    "Q21191270",
    "Q1980247",
    "Q3925766",
    "Q1347347"
   ]
  },
  "revision_id": "2569946872",
  "ancestor_of": "Q137161161",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q2431196",
  "label": "audiovisual work",
  "description": "creative work possessing both a sound and a visual component",
  "aliases": [
   "audial visual work",
   "audial visual works",
   "audial-visual work",
   "audial-visual works",
   "work (audio visual)",
   "work (audio-visual)",
   "work (audiovisual)",
   "works (audio visual)",
   "works (audio-visual)",
   "works (audiovisual)",
   "audio visual work"
  ],
  "claims": {
   "P279": [
    "Q17537576",
    "Q194980",
    "Q106213450",
    "Q110879282",
    "Q110910970"
   ],
   "P1889": [
    "Q10301427",
    "Q114797752"
   ]
  },
  "revision_id": "2515922050",
  "ancestor_of": "Q137161161",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q15416",
  "label": "television program",
  "description": "segment of audiovisual content intended for broadcast and streaming on television",
  "aliases": [
   "television programme",
   "television show",
   "TV program",
   "TV show",
   "TV programme",
   "TV broadcast",
   "television broadcast",
   "T.V. program",
   "T. V. program",
   "T.V. show",
   "T. V. show",
   "T.V. broadcast",
   "T. V. broadcast",
   "television appearance",
   "streaming television"
  ],
  "claims": {
   "P31": [
    "Q110562117"
   ],
   "P279": [
    "Q11578774",
    "Q2431196",
    "Q10301427",
    "Q7725310"
   ],
   "P361": [
    "Q12376699",
    "Q289"
   ],
   "P1889": [
    "Q1407245",
    "Q1555508"
   ]
  },
  "revision_id": "2570981425",
  "ancestor_of": "Q137161161",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~
