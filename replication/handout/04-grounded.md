# Skills Lexicon pilot, grounded run: message 5 of 13 (chunk 04, 3 concepts)

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
`"_meta": {"model": "<your model and version>", "run": "grounded", "chunk": "04", "attempts": 1}`.
If you can make files, send a file named `drafts-grounded-04.jsonl`. Otherwise send one code block marked `jsonl` holding the 3 lines and nothing else. A script will check them afterwards.

---

## Concept 1 of 3: C# (`dbxqhrpv38`)

~~~~text
Concept record:
{
 "id": "dbxqhrpv38",
 "preferred_name": "C#",
 "kind": "programming-language",
 "broad_class": "language",
 "variants": [
  {
   "label": "C Sharp"
  },
  {
   "label": "C Sharp (Programming Language)"
  },
  {
   "label": "C# (Programming Language)"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "tbtzl802aq",
  "name": "ReSharper"
 },
 {
  "id": "l54jfkzunm",
  "name": "Programming"
 },
 {
  "id": "ls6hrpynv0",
  "name": "Java"
 },
 {
  "id": "qb4qnsutxp",
  "name": "C++"
 },
 {
  "id": "cex5ha398q",
  "name": "Design"
 },
 {
  "id": "ly6jzdmqwz",
  "name": "Delphi"
 },
 {
  "id": "d4xxm6t88j",
  "name": "DevOps"
 },
 {
  "id": "kcu5dpjinp",
  "name": "Eiffel"
 },
 {
  "id": "iip9ks8y55",
  "name": "Objective-C"
 },
 {
  "id": "hjzieo2ohv",
  "name": "React"
 },
 {
  "id": "x80b957frq",
  "name": "Ada"
 },
 {
  "id": "dwchdo7ntf",
  "name": "Assembly language"
 },
 {
  "id": "op6iieveb7",
  "name": "Bash"
 },
 {
  "id": "a0h79b66kq",
  "name": "C"
 },
 {
  "id": "wonwpe2z38",
  "name": "F#"
 },
 {
  "id": "xkyic5vgkn",
  "name": "J#"
 },
 {
  "id": "ub71msqw4l",
  "name": "Q#"
 },
 {
  "id": "uct8ix3rbg",
  "name": "Tcl"
 },
 {
  "id": "oeixkjthc3",
  "name": "R"
 },
 {
  "id": "eaovn4ljeo",
  "name": "D"
 },
 {
  "id": "ybdv7l9ewb",
  "name": "Hack"
 },
 {
  "id": "np8jq1gkrj",
  "name": "F*"
 },
 {
  "id": "n29960itit",
  "name": "Go"
 },
 {
  "id": "kb3pruwri8",
  "name": "Oz"
 },
 {
  "id": "ztt7xizgr8",
  "name": "Scala"
 },
 {
  "id": "rw1cn65xyv",
  "name": "COBOL"
 },
 {
  "id": "rfrqfpigh3",
  "name": "OCaml"
 },
 {
  "id": "r9tfnc7x3j",
  "name": "CLIST"
 },
 {
  "id": "gk12ir4ef9",
  "name": "BASIC"
 },
 {
  "id": "znqe62lhes",
  "name": "AWK"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "q1n9huan/global-job-market-postings-dataset@v1/foreign_jobs.release_candidate_v14_enriched.kaggle.csv:15",
  "source": "kaggle:q1n9huan/global-job-market-postings-dataset (CC0: Public Domain), column description",
  "text": "Job title: Senior DevOps Engineer. devops|.net|android|aws|azure|c|c#|c++|data science|golang|ios|java|javascript|kubernetes|node.js|php|python|react|ruby/rails|scala|shopify|sql|swift|ui/ux|wordpress|blockchain|ai/ml|automation|project management|react native|rust|product management|unity|electron|spring|data analysis|bash|laravel|e…"
 },
 {
  "id": "maminkheneifar/jobinja-job-listings-26k@v1/Jobinja - Processed.csv:104",
  "source": "kaggle:maminkheneifar/jobinja-job-listings-26k (CC0: Public Domain), column Job Description",
  "text": "ASP.NET Core, Entity Framework, C#, Sql Server"
 },
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:479",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: Nhân Viên Lập Trình (IT Development). [\"MySQL\", \"C#\", \"VB.NET\", \"HTML\", \"ASP.Net\"]"
 },
 {
  "id": "scrapifier/indeed-usa-job-postings@v1/indeed_usa_job_postings.csv:442",
  "source": "kaggle:scrapifier/indeed-usa-job-postings (CC0: Public Domain), column description",
  "text": "Job title: Software Engineer. …cience, or Mathematics • Zero (0) to three (3) years of experience is required. • NAS experience is desired. Required Skills • Knowledge of C#. • Ability to: • Work independently, as well as on a team, in a fast-paced environment. • Navigate complex workflows; research and problem solve; willingness…"
 },
 {
  "id": "priyankamalavade/naukri-jobs-details@v1/naukri_data_analyst_jobs.csv:1139",
  "source": "kaggle:priyankamalavade/naukri-jobs-details (MIT), column Description",
  "text": "Job title: C# Developer. C#, IT services, SAN, Head Business Development, PDF, SOC, SMS, digital transformation"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[
 {
  "title": "C Sharp (programming language)",
  "revision_id": "1369765227",
  "matched_by": "title",
  "text": "C# (/ˌsiː ˈʃɑːrp/ see SHARP) is a general-purpose high-level programming language supporting multiple paradigms. C# encompasses static typing, strong typing, lexically scoped, imperative, declarative, functional, generic, object-oriented (class-based), and component-oriented programming disciplines.\n\nThe principal designers of the C# programming language were Anders Hejlsberg, Scott Wiltamuth, and Peter Golde from Microsoft. It was first widely distributed in July 2000 and was later approved as an international standard by Ecma (ECMA-334) in 2002 and ISO/IEC (ISO/IEC 23270 and 20619) in 2003. Microsoft introduced C# along with .NET Framework and Microsoft Visual Studio, both of which are, technically speaking, closed-source. At the time, Microsoft had no open-source products. Four years later, in 2004, a free and open-source project called Mono began, providing a cross-platform compiler and runtime environment for the C# programming language. A decade later, Microsoft released Visual Studio Code (code editor), Roslyn (compiler), and the unified .NET platform (software framework), all of which support C# and are free, open-source, and cross-platform. Mono also joined Microsoft, but was not merged into .NET.\n\nAs of November 2025, the most recent stable version of the language is C# 14.\n\nDesign goals\n\nThe Ecma standard lists these design goals for C#:\n\nThe language is intended to be a simple, modern, general-purpose, object-oriented programming language.\n\nThe language, and implementations thereof, should provide support for software engineering principles such as strong type checking, array bounds checking, detection of attempts to use uninitialized variables, and automatic garbage collection. Software robustness, durability, and programmer productivity are important.\n\nThe language is intended for use in developing software components suitable for deployment in distributed environments.\n\nPortability is very important for source code and programmers, especially those already familiar with C and C++.\n\nSupport for internationalization is very important.\n\nC# is intended to be suitable for writing applications for both hosted and embedded systems, ranging from the very large that use sophisticated operating systems, down to the very small having dedicated functions.\n\nAlthough C# applications are intended to be economical with regard to memory and processing power requirements, the language was not intended to compete directly on performance and size with C or assembly language.\n\nHistory\n\nDuring the development of the .NET Framework, the class libraries were originally written using a managed code compiler system named Simple Managed C (SMC). In January 1999, Anders Hejlsberg formed a team to build a new language at the time called COOL, which stood for \"C-like Object Oriented Language\".\n\nMicrosoft had considered keeping the name \"COOL(C-like Object Oriented Language)\" as the final name of the language, but chose not to do so for trademark reasons. By the time the .NET project was publicly announced at the July 2000 Professional Developers Conference, the language had been renamed C#, and the class libraries and ASP.NET runtime were ported to C#.\n\nHejlsberg was C#'s principal designer and lead architect at Microsoft, and had been previously involved with the design of Turbo Pascal, Embarcadero Delphi (formerly CodeGear Delphi, Inprise Delphi and Borland Delphi), and Visual J++. In interviews and technical papers, he has stated that flaws in most major programming languages (e.g. C++, Java, Delphi, and Smalltalk) drove the fundamentals of the Common Language Runtime (CLR), which, in turn, drove the design of the C# language.\n\nJames Gosling, who created the Java programming language in 1994, and Bill Joy, a co-founder of Sun Microsystems, the originator of Java, called C# an \"imitation\" of Java; Gosling further said: \"[C# is] sort of Java with reliability, productivity and security deleted.\" \n\nIn July 2000, Hejlsberg said that C# is \"not a Java clone\" and is \"much closer to C++\" in its design.\n\nSince the release of C# 2.0 in November 2005, the C# and Java languages have evolved on increasingly divergent trajectories, becoming two quite different languages. One of the first major departures came with the addition of generics to both languages, with vastly different implementations. C# uses reification to provide \"first-class\" generic objects that can be used like any other class, with code generation performed at class-load time.\n\nC# has also added several major features to accommodate functional-style programming, culminating in the LINQ extensions released with C# 3.0 and its supporting framework of lambda expressions, extension methods, and anonymous types. These features enable C# programmers to use functional programming techniques, such as closures, when it is advantageous to their application. The LINQ extensions and the functional imports help developers reduce the amount of boilerplate code included in common tasks such as querying a database, parsing an XML file, or searching through a data structure, shifting the emphasis onto the actual program logic to help improve readability and maintainability.\n\nC# used to have a mascot called Andy (named after Anders Hejlsberg). It was retired on January 29, 2004.\n\nC# was originally submitted to the ISO/IEC JTC 1 subcommittee SC 22 for review, under ISO/IEC 23270:2003, was withdrawn and was then approved under ISO/IEC 23270:2006. The 23270:2006 is withdrawn under 23270:2018 and approved with this version.\n\nName\n\nMicrosoft first used the name C# in 1988 for a variant of the C language designed for incremental compilation. That project was not completed, and the name was later reused.\n\nThe name \"C sharp\" was inspired by the musical notation whereby a sharp symbol indicates that the written note should be made a semitone higher in pitch.\nThis is similar to the language name of C++, where \"++\" indicates that a variable should be incremented by 1 after being evaluated. The sharp symbol also resembles a ligature of four \"+\" symbols (in a two-by-two grid), further implying that the language is an increment of C++.\n\nDue to technical limits of display (standard fonts, browsers, etc.), and most keyboard layouts lacking a sharp symbol (U+266F ♯ MUSIC SHARP SIGN (&sharp;)), the number sign (U+0023 # NUMBER SIGN (&num;)) was chosen to approximate the sharp symbol in the written name of the programming language.\nThis convention is reflected in the ECMA-334 C# Language Specification.\n\nThe \"sharp\" suffix has been used by a number of other Microsoft .NET compatible/compliant languages that are variants of existing languages, including J# (a .NET language also designed by Microsoft that is derived from Java 1.1), A# (from Ada), and the functional programming language F#. The original implementation of Eiffel for .NET was called Eiffel#, a name retired since the full Eiffel language is now supported. The suffix has also been used for libraries, such as Gtk# (a .NET wrapper for GTK and other GNOME libraries) and Cocoa# (a wrapper for Cocoa).\n\nVersions\n\nDevelopment of the text for standards (beginning with C# 6) is done on GitHub. C# 7 was submitted to Ecma and approved in December 2023. As of January 2024, the standard for C# 8 is currently under development, referencing the approved language proposals.\n\nSyntax\n\nThe core syntax of the C# language is similar to that of other C-style languages such as C, Objective-C, C++ and Java, particularly:\n\nSemicolons are used to denote the end of a statement.\n\nCurly brackets are used to group statements. Statements are commonly grouped into methods (functions), methods into classes, and classes into namespaces.\n\nVariables are assigned using an equals sign, but compared using two consecutive equals signs.\n\nSquare brackets are used with arrays, both to declare them and to get a value at a given index in one of them.\n\n\"class\", \"int\" and \"void\" are used to define large-scale (usually main) program functions in scripts most of the time in C-style computer programming languages.\n\nDistinguishing features\n\nSome notable features of C# that distinguish it from C, C++, and Java where noted, are:\n\nPortability\n\nBy design, C# is the programming language that most directly reflects the underlying Common Language Infrastructure (CLI). Most of its intrinsic types correspond to value-types implemented by the CLI framework. However, the language specification does not state the code generation requirements of the compiler: that is, it does not state that a C# compiler must target a Common Language Runtime (CLR), or generate Common Intermediate Language (CIL), or generate any other specific format. Some C# compilers can also generate machine code like traditional compilers of Objective-C, C, C++, Assembly and Fortran.\n\nTyping\n\nC# supports strongly, implicitly typed variable declarations with the keyword var, and implicitly typed arrays with the keyword new[] followed by a collection initializer.\n\nIts type system is split into two families: Value types, like the built-in numeric types and user-defined structs, which are automatically handed over as copies when used as parameters, and reference types, including arrays, instances of classes, and strings, which only hand over a pointer to the respective object. Due to their special handling of the equality operator and their immutability, strings will nevertheless behave as if they were values, for all practical purposes. The programmer can even use them as case labels. Where necessary, value types will be boxed automatically.\n\nC# supports a strict Boolean data type, bool. Statements that take conditions, such as while and if, require an expression of a type that evaluates to the true boolean value. While C++ also has a Boolean type, it can be freely converted to and from integers, and expressions such as if (a) require only that a is convertible to bool, allowing a to be an int, or a pointer. C# disallows this \"integer meaning true or false\" approach, on the grounds that forcing programmers to use expressions that return exactly bool can prevent certain types of programming mistakes such as if (a = b) (use of assignment = instead of equality ==).\n\nC# is more type safe than C++. The only implicit conversions by default are those that are considered safe, such as widening of integers. This is enforced at compile-time, during just-in-time compilation, and, in some cases, at runtime. No implicit conversions occur between Booleans and integers, nor between enumeration members and integers (except for literal 0, which can be implicitly converted to any enumerated type). Any user-defined conversion must be explicitly marked as explicit or implicit, unlike C++ copy constructors and conversion operators, which are both implicit by default.\n\nC# has explicit support for covariance and contravariance in generic types, unlike C++ which has some degree of support for contravariance simply through the semantics of return types on virtual methods.\n\nEnumeration members are placed in their own scope.\n\nThe C# language does not allow for global variables or functions. All methods and members must be declared within classes. Static members of public classes can substitute for global variables and functions.\n\nLocal variables cannot shadow variables of the enclosing block, unlike C and C++, but may shadow type-level names.\n\nMetaprogramming\n\nMetaprogramming can be achieved in several ways:\n\nReflection is supported through .NET APIs, which enable scenarios such as type metadata inspection and dynamic method invocation.\n\nExpression trees represent code as an abstract syntax tree, where each node is an expression that can be inspected or executed. This enables dynamic modification of executable code at runtime. Expression trees introduce some homoiconicity to the language.\n\nAttributes, in C# parlance, are metadata that can be attached to types, members, or entire assemblies, equivalent to annotations in Java. Attributes are accessible both to the compiler and to code through reflection, allowing them to adjust their behaviour. Many of the native attributes duplicate the functionality of GCC's and VisualC++'s platform-dependent preprocessor directives.\n\nSystem.Reflection.Emit namespace, which contains classes that emit metadata and CIL (types, assemblies, etc.) at runtime.\n\nThe .NET Compiler Platform (Roslyn) provides API access to language compilation services, allowing for the compilation of C# code from within .NET applications. It exposes APIs for syntactic (lexical) analysis of code, semantic analysis, dynamic compilation to CIL, and code emission.\n\nSource generators, a feature of the Roslyn C# compiler, enable compile time metaprogramming. During the compilation process, developers can inspect the code being compiled with the compiler's API and pass additional generated C# source code to be compiled.\n\nMethods and functions\n\nA method in C# is a member of a class that can be invoked as a function, rather than the mere value-holding capability of a field, i.e., class or instance variable. As in other syntactically similar languages, such as C++ and ANSI C, the signature of a method is a declaration comprising in order: any optional accessibility keywords (such as private), the explicit specification of its return type (such as int, or the keyword void if no value is returned), the name of the method, and finally, a parenthesized sequence of comma-separated parameter specifications, each consisting of a parameter's type, its formal name and optionally, a default value to be used whenever none is provided. Different from most other languages, call-by-reference parameters have to be marked both at the function definition and at the calling site, and the programmer can choose between ref and out, the latter allowing handing over an uninitialized variable which will have a definite value on return. Additionally, the programmer can specify a variable-sized argument list by applying the params keyword to the last parameter. Certain specific kinds of methods, such as those that simply get or set a field's value by returning or assigning it, do not require an explicitly stated full signature, but in the general case, the definition of a class includes the full signature declaration of its methods.\n\nLike C++, and unlike Java, C# programmers must use the scope modifier keyword virtual to allow methods to be overridden by subclasses. Unlike C++, the programmer must explicitly specify the keyword override when doing so. This is supposed to avoid confusion between overriding and newly overloading a function, i.e., hiding the former implementation. To do the latter, the programmer has to specify the new keyword. The keyword sealed can be used to disallow further overrides for individual methods or whole classes.\n\nExtension methods in C# allow programmers to use static methods as if they were methods from a class's method table, allowing programmers to virtually add instance methods to a class that they feel should exist on that kind of objects (and instances of the respective derived classes).\n\nThe type dynamic allows for run-time method binding, allowing for JavaScript-like method calls and run-time object composition.\n\nC# has support for strongly-typed function pointers via the keyword delegate. Like the Qt framework's pseudo-C++ signal and slot, C# has semantics specifically surrounding publish-subscribe style events, though C# uses delegates to do so. Unlike fields, event variables can be part of an interface, because they technically consist of two default functions to add and remove to-be-called delegates.\n\nC# offers Java-like synchronized method calls, via the attribute [MethodImpl(MethodImplOptions.Synchronized)], and has support for mutually-exclusive locks via the keyword lock.\n\nProperties\n\nC# supports classes with properties. The properties can be simple accessor functions with a backing field, or implement arbitrary getter and setter functions. A property is read-only if there's no setter. Like with fields, there can be class and instance properties. The underlying methods can be virtual or abstract like any other method.\n\nSince C# 3.0 the syntactic sugar of auto-implemented properties is available, where the accessor (getter) and mutator (setter) encapsulate operations on a single field of a class.\n\nNamespaces\n\nA C# namespace provides the same level of code isolation as a Java package or a C++ namespace, with rules and features very similar to a package. Namespaces can be imported with the \"using\" syntax.\n\nMemory access\n\nIn C#, memory address pointers can only be used within blocks specifically marked as unsafe, and programs with unsafe code need appropriate permissions to run. Most object access is done through safe object references, which always either point to a \"live\" object or have the well-defined null value; it is impossible to obtain a reference to a \"dead\" object (one that has been garbage collected), or to an arbitrary block of memory. An unsafe pointer can point to an instance of an unmanaged value type that does not contain any references to objects subject to garbage collections such as class instances, arrays or strings. Code that is not marked as unsafe can still store and manipulate pointers through the System.IntPtr type, but it cannot dereference them.\n\nManaged memory cannot be explicitly freed; instead, it is automatically garbage collected. Garbage collection addresses the problem of memory leaks by freeing the programmer of responsibility for releasing memory that is no longer needed in most cases. Code that retains references to objects longer than is required can still experience higher memory usage than necessary, however once the final reference to an object is released the memory is available for garbage collection.\n\nExceptions\n\nA range of standard exceptions are available to programmers. Methods in standard libraries regularly throw system exceptions in some circumstances and the range of exceptions thrown is normally documented. Custom exception classes can be defined for classes allowing handling to be put in place for particular circumstances as needed.\n\nThe syntax for handling exceptions is the following:try\n{\n // something\n}\ncatch (Exception ex)\n{\n // if error do this\n}\nfinally\n{\n // always executes, regardless of error occurrence\n}\n\nThis is usually called a \"try-catch\" code block, because of the \"try\" and \"catch\" functions being used and accessible on all C# versions. The \"finally\" part can be left out. If inspecting the error details is not required, the (Exception ex) parameter can be omitted as well. Also, there can be several \"catch\" parts handling different kinds of exceptions.\n\nChecked exceptions are not present in C# (in contrast to Java). This has been a conscious decision based on the issues of scalability and version management.\n\nPolymorphism\n\nUnlike C++, C# does not support multiple inheritance, although a class can implement any number of \"interfaces\" (fully abstract classes). This was a design decision by the language's lead architect to avoid complications and to simplify architectural requirements throughout CLI.\n\nWhen implementing multiple interfaces that contain a method with the same name and taking parameters of the same types in the same order, i.e., the same signature, similar to Java, C# allows both a single method to cover all interfaces and, if necessary, specific methods for each interface.\n\nC# also offers function overloading (a.k.a. ad-hoc-polymorphism), i.e., methods with the same name, but distinguishable signatures. Unlike Java, C# additionally supports operator overloading.\n\nSince version 2.0, C# offers parametric polymorphism, i.e., classes with arbitrary or constrained type parameters, e.g., List<T>, a variable-sized array which only can contain elements of type T. There are certain kinds of constraints the programmer can specify for the type parameters: Has to be type X (or one derived from it), has to implement a certain interface, has to be a reference type, has to be a value type, has to implement a public parameterless constructor. Most of them can be"
 },
 {
  "title": "Musical note",
  "revision_id": "1378230120",
  "matched_by": "redirect-minus-qualifier",
  "text": "In music, notes are distinct and isolatable sounds that act as the most basic building blocks for nearly all of music. This discretization facilitates performance, comprehension, and analysis. Notes may be visually communicated by writing them in musical notation.\n\nNotes can distinguish the general pitch class or the specific pitch played by a pitched instrument. Although this article focuses on pitch, notes for unpitched percussion instruments distinguish between different percussion instruments (and/or different manners to sound them) instead of pitch. Note value expresses the relative duration of the note in time. Dynamics for a note indicate how loud to play them. Articulations may further indicate how performers should shape the attack and decay of the note and express fluctuations in a note's timbre and pitch. Notes may even distinguish the use of different extended techniques by using special symbols.\n\nThe term note can refer to a specific musical event, for instance when saying the song \"Happy Birthday to You\", begins with two notes of identical pitch. Or more generally, the term can refer to a class of identically sounding events, for instance when saying \"the song begins with the same note repeated twice.\"\n\nDistinguishing duration\n\nA note can have a note value that indicates the note's duration relative to the musical meter. In order of halving duration, these values are:\n\nLonger note values (e.g. the longa; twice the length of a breve) and shorter note values (e.g. the two hundred fifty-sixth note) do exist, but are very rare in modern times. These durations can further be subdivided using tuplets or extended using dots. Furthermore, a tie can combine two notes together to create a more specific duration which cannot be represented by a single note's value.\n\nA rhythm is formed from a sequence in time of consecutive notes and rests (the spaces between notes) of various durations. Rhythms are agnostic to pitches, so if a melody is transposed to a different scale, its rhythm will remain constant.\n\nDistinguishing pitch\n\nDistinguishing pitches of a scale\n\nMusic theory in most European countries and others use the solfège naming convention. Fixed do uses the syllables re–mi–fa–sol–la–si specifically for the C major scale, while movable do labels notes of any major scale with that same order of syllables.\n\nAlternatively, particularly in English- and some Dutch-speaking regions, and certainly in all of Germany, pitch classes are typically represented by the first seven letters of the Latin alphabet (A, B, C, D, E, F and G), corresponding to the A minor scale. Several European countries, including Germany and Czechia, use H instead of B (see § 12-tone chromatic scale for details). Byzantium used the names Pa–Vu–Ga–Di–Ke–Zo–Ni (Πα–Βου–Γα–Δι–Κε–Ζω–Νη). A single note is sometimes called a monad.\n\nIn traditional Indian music, musical notes are called svaras and commonly represented using the seven notes, Sa, Re, Ga, Ma, Pa, Dha and Ni.\n\nWriting notes on a staff\n\nIn a score, each note is assigned a specific vertical position on a staff position (a line or space) on the staff, as determined by the clef. Each line or space is assigned a note name. These names are memorized by musicians and allow them to know at a glance the proper pitch to play on their instruments.\nMusical scores are temporarily disabled due to a security issue. See Help:Score.\n\nThe staff above shows the notes C, D, E, F, G, A, B, C and then in reverse order, with no key signature or accidentals.\n\nAccidentals\n\nNotes that belong to the diatonic scale relevant in a tonal context are called diatonic notes. Notes that do not meet that criterion are called chromatic notes or accidentals. Accidental symbols visually communicate a modification of a note's pitch from its tonal context. Most commonly, the sharp symbol (♯) raises a note by a half step, while the flat symbol (♭) lowers a note by a half step. This half step interval is also known as a semitone (which has an equal temperament frequency ratio of √2 ≅ 1.0595). The natural symbol (♮) indicates that any previously applied accidentals should be cancelled. Advanced musicians use the double-sharp symbol () to raise the pitch by two semitones, the double-flat symbol () to lower it by two semitones, and even more advanced accidental symbols (e.g. for quarter tones). Accidental symbols are placed to the right of a note's letter when written in text (e.g. F♯ is F-sharp, B♭ is B-flat, and C♮ is C natural), but are placed to the left of a note's head when drawn on a staff.\n\nSystematic alterations to any of the 7 lettered pitch classes are communicated using a key signature. When drawn on a staff, accidental symbols are positioned in a key signature to indicate that those alterations apply to all occurrences of the lettered pitch class corresponding to each symbol's position. Additional explicitly-noted accidentals can be drawn next to noteheads to override the key signature for all subsequent notes with the same lettered pitch class in that bar. However, this effect does not accumulate for subsequent accidental symbols for the same pitch class.\n\n12-tone chromatic scale\n\nAssuming enharmonicity, accidentals can create pitch equivalences between different notes (e.g. the note B♯ represents the same pitch as the note C). Thus, a 12-note chromatic scale adds 5 pitch classes in addition to the 7 lettered pitch classes.\n\nThe following chart lists names used in different countries for the 12 pitch classes of a chromatic scale built on C. Their corresponding symbols are in parentheses. Differences between German and English notation are highlighted in bold typeface. Although the English and Dutch names are different, the corresponding symbols are identical.\n\nDistinguishing pitches of different octaves\n\nTwo pitches that are any whole number of octaves apart (i.e. their fundamental frequencies are in a ratio equal to a power of two) are perceived as very similar. Because of that, all notes with these kinds of relations can be grouped under the same pitch class and are often given the same name.\n\nThe top note of a musical scale is the bottom note's second harmonic and has double the bottom note's frequency. Because both notes belong to the same pitch class, they are often called by the same name. That top note may also be referred to as the \"octave\" of the bottom note, since an octave is the interval between a note and another with double frequency.\n\nMiddle C\n\nMusical scores are temporarily disabled due to a security issue. See Help:Score.\nMiddle C centrallyset on a grand staff\n\nMiddle C is often used as a common reference point when discussing octaves. This is the C between the typical treble and bass staves; either one ledger line below the treble staff, or one ledger line above the bass. In standard tuning it has a pitch of 261.626 Hz.\n\nMiddle C is a convenient reference, as it can be played on most common instruments. It can be sung by both male and female singers. It also falls near the middle of a standard 88-key piano.\n\nThe most common tuning, the A440 pitch standard, defines the A above middle C to be exactly 440 Hz.\n\nScientific versus Helmholtz pitch notation\n\nSeveral nomenclature systems for differentiating pitches that have the same pitch class but which fall into different octaves.\n\nScientific pitch notation, where a pitch class letter (C, D, E, F, G, A, B) is followed by a subscript Arabic numeral designating a specific octave.\n\nMiddle C is named C4 and is the start of the 4th octave.\n\nHigher octaves use successively higher number and lower octaves use successively lower numbers (including negative numbers)\n\nThe lowest note on most pianos is A0, the highest is C8.\n\nHelmholtz pitch notation, which distinguishes octaves using prime symbols and letter case of the pitch class letter.\n\nThe scale is based on the C one octave below middle C (C3 in scientific pitch notation), sometimes called *tenor C*.\n\nThe octave starting at tenor C are written as lower case letters, so tenor C itself is written c in Helmholtz notation.\n\nHigher octaves are notated by appending additional prime symbols above the letter. Thus, middle C is written c′, the next octave c′′, etc.\n\nOctaves below tenor C are written with upper case letters, with sub-prime symbols prepended for each additional octave. Thus the octaves below tenor C are written C, ͵C, ͵͵C, etc.\n\nA number of typographic variants exist for Helmholtz notation. For instance, primes and sub-primes may be replaced with apostrophe and comma characters, sub-primes can be placed either before or after the note letter, or letters can be repeated (͵͵C = C͵͵ = C,, = CCC).\n\nOctaves are also named (see table below).\n\nThe MIDI standard for electronic musical instruments doesn't specifically designate pitch classes, but instead names pitches sequentially.\n\nThe supported lowest note, C−1 (≈ 8.1758 Hz), is numbered 0.\n\nSubsequent notes are numbered chromatically to the highest, number 127 (G9 ≈ 12,544 Hz).\n\nAlthough the MIDI standard is clear, the octaves actually played by any one MIDI device don't necessarily match the octaves shown below, especially in older instruments.\n\nFor instance, the standard 440 Hz tuning pitch is named A4 in scientific notation, a′ in Helmholtz notation, and number 69 in MIDI.\n\nPitch frequency in hertz\n\nPitch is associated with the frequency of physical oscillations measured in hertz (Hz) representing the number of these oscillations per second. While notes can have any arbitrary frequency, notes in more consonant music tend to have pitches with simpler mathematical ratios to each other.\n\nWestern music defines pitches around a central reference \"concert pitch\" of A4, currently standardized as 440 Hz. Notes played in tune with the 12 equal temperament system will be an integer number of half-steps above (positive ) or below (negative ) that reference note, and thus have a frequency of:\n\nOctaves automatically yield powers of two times the original frequency, since can be expressed as when is a multiple of 12 (with being the number of octaves up or down). Thus the above formula reduces to yield a power of 2 multiplied by 440 Hz:\n\nLogarithmic scale\n\nThe base-2 logarithm of the above frequency–pitch relation conveniently results in a linear relationship with or :\n\nWhen dealing specifically with intervals (rather than absolute frequency), the constant can be conveniently ignored, because the difference between any two frequencies and in this logarithmic scale simplifies to:\n\nCents are a convenient unit for humans to express finer divisions of this logarithmic scale that are 1⁄100 of an equally-tempered semitone. Since one semitone equals 100 cents, one octave equals 12 ⋅ 100 cents = 1200 cents. Cents correspond to a difference in this logarithmic scale, however in the regular linear scale of frequency, adding 1 cent corresponds to multiplying a frequency by √2 (≅ 1.000578).\n\nMIDI\n\nFor use with the MIDI (Musical Instrument Digital Interface) standard, a frequency mapping is defined by:\n\nwhere is the MIDI note number. 69 is the number of semitones between C−1 (MIDI note 0) and A4.\n\nConversely, the formula to determine frequency from a MIDI note is:\n\nPitch names and their history\n\nMusic notation systems have used letters of the alphabet for centuries. The 6th century philosopher Boethius is known to have used the first fourteen letters of the classical Latin alphabet (the letter J did not exist until the 16th century),\n\nA   B   C   D   E   F   G   H   I   K   L   M   N   O\n\nto signify the notes of the two-octave range that was in use at the time and in modern scientific pitch notation are represented as\n\nA2   B2   C3   D3   E3   F3   G3   A3   B3   C4   D4   E4   F4   G4\n\nThough it is not known whether this was his devising or common usage at the time, this is nonetheless called Boethian notation. Although Boethius is the first author known to use this nomenclature in the literature, Ptolemy wrote of the two-octave range five centuries before, calling it the perfect system or complete system – as opposed to other, smaller-range note systems that did not contain all possible species of octave (i.e., the seven octaves starting from A, B, C, D, E, F, and G). A modified form of Boethius' notation later appeared in the Dialogus de musica (ca. 1000) by Pseudo-Odo, in a discussion of the division of the monochord.\n\nFollowing this, the range (or compass) of used notes was extended to three octaves, and the system of repeating letters A–G in each octave was introduced, these being written as lower-case for the second octave (a–g) and double lower-case letters for the third (aa–gg). When the range was extended down by one note, to a G, that note was denoted using the Greek letter gamma (Γ), the lowest note in Medieval music notation. (It is from this gamma that the French word for scale, gamme derives, and the English word gamut, from \"gamma-ut\".)\n\nThe remaining five notes of the chromatic scale (the black keys on a piano keyboard) were added gradually; the first being B♭, since B was flattened in certain modes to avoid the dissonant tritone interval. This change was not always shown in notation, but when written, B♭ (B flat) was written as a Latin, cursive \"𝒷\", and B♮ (B natural) a Gothic script (known as Blackletter) or \"hard-edged\" 𝔟. These evolved into the modern flat (♭) and natural (♮) symbols respectively.\n\nB♭, B and H\n\nIn parts of Europe, including Germany, Czechia, Slovakia, Poland, Hungary, Norway, Denmark, Serbia, Croatia, Slovenia, Finland, and Iceland (as well as Sweden before the 1990s), the Gothic 𝔟 transformed into the letter h. Therefore, in current German music terminology, H is used instead of B♮ (B natural), and B instead of B♭ (B flat).\n\nSystem \"do–re–mi–fa–sol–la–si\"\n\nIn Italian, Portuguese, Spanish, French, Romanian, Greek, Albanian, Russian, Mongolian, Flemish, Persian, Arabic, Hebrew, Ukrainian, Bulgarian, Turkish and Vietnamese the note names are do–re–mi–fa–sol–la–si rather than C–D–E–F–G–A–B. These names follow the original names reputedly given by Guido d'Arezzo, who had taken them from the first syllables of the first six musical phrases of a Gregorian chant melody Ut queant laxis, whose successive lines began on the appropriate scale degrees. These became the basis of the solfège system. For ease of singing, the name ut was largely replaced by do (most likely from the beginning of Dominus, \"Lord\"), though ut is still used in some places. It was the Italian musicologist and humanist Giovanni Battista Doni (1595–1647) who successfully promoted renaming the name of the note from ut to do. For the seventh degree, the name si (from Sancte Iohannes, St. John, to whom the hymn is dedicated), though in some regions the seventh is named ti (again, easier to pronounce while singing).\n\nSee also"
 },
 {
  "title": "C-sharp minor",
  "revision_id": "1368626729",
  "matched_by": "redirect-minus-qualifier",
  "text": "C-sharp minor is a minor scale based on C♯, with the pitches C♯, D♯, E, F♯, G♯, A, and B. Its key signature consists of four sharps.\n\nThe C-sharp natural minor scale is:\n\nMusical scores are temporarily disabled due to a security issue. See Help:Score.\n\nChanges needed for the melodic and harmonic versions of the scale are written in with accidentals as necessary. The C-sharp harmonic minor and melodic minor scales are:\n\nMusical scores are temporarily disabled due to a security issue. See Help:Score.\nMusical scores are temporarily disabled due to a security issue. See Help:Score.\n\nIts relative major is E major. Its parallel major, C-sharp major, would require seven sharps and is usually written as the enharmonic key of D-flat major instead, with five flats.\n\nScale degree chords\n\nThe scale degree chords of C-sharp minor are:\n\nTonic – C-sharp minor\n\nSupertonic – D-sharp diminished\n\nMediant – E major\n\nSubdominant – F-sharp minor\n\nDominant – G-sharp minor\n\nSubmediant – A major\n\nSubtonic – B major\n\nClassical music in this key\n\nThere are only two known symphonies in the 18th century written in this key. One of them is by Joseph Martin Kraus, who appears to have found the key difficult since he later rewrote it in C minor. In the following two centuries, C-sharp minor symphonies remained rare. Notable examples are the second movement Adagio of Anton Bruckner's Symphony No. 7, the first movement of Gustav Mahler's Symphony No. 5 and Prokofiev's Symphony No. 7.\n\nThis key occurs more often in piano literature from the 18th century onwards. Domenico Scarlatti wrote just two keyboard sonatas in C-sharp minor, K. 246 and K. 247. After Beethoven's Piano Sonata No. 14 (Moonlight Sonata), the key became more frequent in the piano repertoire. Beethoven himself used this key again in the outer movements of his String Quartet No. 14 (Op. 131, 1826). Even so, Johannes Brahms still felt the need to rewrite his C-sharp minor piano quartet in C minor, which was published as Piano Quartet No. 3 in C minor, Op. 60. The last intermezzo from his Three Intermezzi for piano, Op. 117 is in C-sharp minor.\n\nAlkan composed the second movement (Adagio) for Concerto for Solo Piano in C-sharp minor.\n\nFrédéric Chopin often wrote in this key: examples include the Fantaisie-Impromptu, Études Op. 10, No. 4 and Op. 25, No. 7, Scherzo No. 3 (Op. 39), Waltz Op. 64, No. 2, Polonaise Op. 26 No. 1, the Prelude opus 45 and Nocturnes No. 7 (Op. 27, No. 1) and No. 20 (Lento con gran espressione). More examples of works in C-sharp minor include Rachmaninoff's Prelude in C-sharp minor (Op. 3, No. 2), Scriabin's Étude in C-sharp minor, Op. 2, No. 1, Franz Liszt's Hungarian Rhapsody No. 2, and Tchaikovsky's Piano Sonata in C-sharp minor.\n\nPiano concertos written in C-sharp minor include Poulenc's Piano Concerto in C-sharp minor, FP 146 (1949), Erich Wolfgang Korngold's Piano Concerto for the Left Hand, Op. 17, Nikolai Rimsky-Korsakov's Piano Concerto, and others by Ferdinand Ries, Xaver Scharwenka, Amy Beach, Miriam Hyde and Issay Dobrowen.\n\nFranz Berwald and Dimitri Shostakovich wrote violin concertos in C-sharp minor.\n\nJules Van Nuffel wrote his psalm setting In convertendo Dominus for choir and organ in C-sharp minor.\n\nC-sharp minor is often used as the parallel minor of D-flat major, especially since D-flat major's real parallel minor, D-flat minor, would have eight flats including one double-flat. For example, in his Prelude No. 15 in D-flat major (\"Raindrop\"), Frédéric Chopin switches from D-flat major to C-sharp minor for the middle section in the parallel minor, while in his Fantaisie-Impromptu and Scherzo No. 3, primarily in C-sharp minor, he switches to D-flat major for the middle section for the opposite reason. Claude Debussy likewise switches from D-flat major to C-sharp minor in the significant section in his famous \"Clair de lune\" for a few measures. Antonín Dvořák's New World Symphony also switches to C-sharp minor for a while for the significant section in the slow movement.\n\nSee also"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q2370",
  "label": "C#",
  "description": "multi-paradigm (object-oriented) programming language",
  "aliases": [
   "c#",
   "Microsoft Java"
  ],
  "claims": {
   "P31": [
    "Q9143",
    "Q12772052",
    "Q28922858",
    "Q211496",
    "Q28920813"
   ],
   "P279": [
    "Q651794"
   ],
   "P361": [
    "Q5289",
    "Q21622213"
   ]
  },
  "revision_id": "2567967158",
  "value_labels": {
   "Q9143": "programming language",
   "Q12772052": "multi-paradigm programming language",
   "Q28922858": "class-based programming language",
   "Q211496": "high-level programming language",
   "Q28920813": "event-driven programming language",
   "Q651794": "compiled language",
   "Q5289": "",
   "Q21622213": ""
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q263478",
  "label": "note sign",
  "description": "sign used in musical notation to describe a pitched sound (frequency + duration)",
  "aliases": [
   "musical note",
   "music note"
  ],
  "claims": {
   "P31": [
    "Q115211517"
   ],
   "P279": [
    "Q3241972",
    "Q151411"
   ],
   "P361": [
    "Q233861"
   ],
   "P527": [
    "Q4122143",
    "Q572837"
   ],
   "P1889": [
    "Q1760309",
    "Q586277",
    "Q137473569",
    "Q118819"
   ]
  },
  "revision_id": "2517552907",
  "value_labels": {
   "Q115211517": "musical concept",
   "Q3241972": "character",
   "Q151411": "designation",
   "Q233861": "musical notation",
   "Q4122143": "note head",
   "Q572837": "stem",
   "Q1760309": "pitch class",
   "Q586277": "degree",
   "Q137473569": "musical pitch",
   "Q118819": "pitch"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q283749",
  "label": "C-sharp minor",
  "description": "tonality",
  "aliases": [],
  "claims": {
   "P31": [
    "Q12827391",
    "Q192822"
   ],
   "P460": [
    "Q3303490"
   ]
  },
  "revision_id": "2550825170",
  "value_labels": {
   "Q12827391": "minor mode",
   "Q192822": "tonal system",
   "Q3303490": "D-flat minor"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q9143",
  "label": "programming language",
  "description": "language for communicating instructions to a machine",
  "aliases": [
   "computer language",
   "computer programming language",
   "coding language",
   "computer programming"
  ],
  "claims": {
   "P31": [
    "Q66747126",
    "Q137527772"
   ],
   "P279": [
    "Q629206"
   ],
   "P361": [
    "Q68"
   ],
   "P527": [
    "Q1152399",
    "Q25346349",
    "Q1199356",
    "Q865760"
   ],
   "P1889": [
    "Q4117406",
    "Q173341",
    "Q189224",
    "Q629206",
    "Q77654221"
   ]
  },
  "revision_id": "2570899010",
  "ancestor_of": "Q2370",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q12772052",
  "label": "multi-paradigm programming language",
  "description": "programming language type",
  "aliases": [],
  "claims": {
   "P31": [
    "Q116481801"
   ],
   "P279": [
    "Q9143"
   ]
  },
  "revision_id": "2552000821",
  "ancestor_of": "Q2370",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q28922858",
  "label": "class-based programming language",
  "description": "programming language",
  "aliases": [],
  "claims": {
   "P31": [
    "Q116481801"
   ],
   "P279": [
    "Q9143",
    "Q899523"
   ]
  },
  "revision_id": "2512265637",
  "ancestor_of": "Q2370",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q211496",
  "label": "high-level programming language",
  "description": "programming language with strong abstraction from details of hardware",
  "aliases": [
   "high-level language",
   "HLL"
  ],
  "claims": {
   "P31": [
    "Q116481801"
   ],
   "P279": [
    "Q9143"
   ]
  },
  "revision_id": "2564820107",
  "ancestor_of": "Q2370",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q28920813",
  "label": "event-driven programming language",
  "description": "kind of programming language",
  "aliases": [],
  "claims": {
   "P31": [
    "Q116481801"
   ],
   "P279": [
    "Q9143"
   ]
  },
  "revision_id": "2362182530",
  "ancestor_of": "Q2370",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q651794",
  "label": "compiled language",
  "description": "a programming language implemented with a compiler that translates source code into a binary executable form",
  "aliases": [
   "compiled",
   "compiled programming language"
  ],
  "claims": {
   "P31": [
    "Q116481801"
   ],
   "P279": [
    "Q9143",
    "Q188267"
   ]
  },
  "revision_id": "2554781751",
  "ancestor_of": "Q2370",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q66747126",
  "label": "computer science term",
  "description": "technical term; word or phrase that is part of computer science terminology",
  "aliases": [
   "computer science concept",
   "computer term",
   "informatics term"
  ],
  "claims": {
   "P31": [
    "Q19478619",
    "Q137426749",
    "Q137429456"
   ],
   "P279": [
    "Q12812139",
    "Q999234",
    "Q151885"
   ],
   "P361": [
    "Q3457057"
   ]
  },
  "revision_id": "2547355639",
  "ancestor_of": "Q2370",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q137527772",
  "label": "type of computer language",
  "description": "metaclass",
  "aliases": [],
  "claims": {
   "P31": [
    "Q24017414"
   ],
   "P279": [
    "Q20829075"
   ]
  },
  "revision_id": "2558752535",
  "ancestor_of": "Q2370",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q629206",
  "label": "computer language",
  "description": "formal language used in communication with a computer",
  "aliases": [
   "computing language"
  ],
  "claims": {
   "P31": [
    "Q20829075"
   ],
   "P279": [
    "Q192161",
    "Q15621286",
    "Q235557",
    "Q3247505",
    "Q1371819"
   ],
   "P1889": [
    "Q9143",
    "Q1122600"
   ]
  },
  "revision_id": "2563920475",
  "ancestor_of": "Q2370",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q116481801",
  "label": "type of programming language",
  "description": "Wikidata metaclass",
  "aliases": [
   "kind of programming language",
   "programming language type",
   "programming language category",
   "category of programming languages"
  ],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q21146257",
    "Q137527772"
   ]
  },
  "revision_id": "2555835128",
  "ancestor_of": "Q2370",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q899523",
  "label": "object-based language",
  "description": "programming language",
  "aliases": [
   "OOP programming language",
   "OOP",
   "object-oriented programming language",
   "object-oriented language"
  ],
  "claims": {
   "P31": [
    "Q116481801"
   ],
   "P279": [
    "Q9143"
   ]
  },
  "revision_id": "2515887381",
  "ancestor_of": "Q2370",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q188267",
  "label": "programming paradigm",
  "description": "category of programming languages according to what methodology of designing and implementing programs their features support",
  "aliases": [],
  "claims": {
   "P279": [
    "Q28643",
    "Q962139"
   ]
  },
  "revision_id": "2538683798",
  "ancestor_of": "Q2370",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q115211517",
  "label": "musical concept",
  "description": "type of artistic concept",
  "aliases": [],
  "claims": {
   "P279": [
    "Q63539947"
   ]
  },
  "revision_id": "2541599296",
  "ancestor_of": "Q263478",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q3241972",
  "label": "character",
  "description": "symbol or sign (concept unrelated to computing)",
  "aliases": [
   "sign",
   "typographic symbol",
   "typographical mark",
   "symbol",
   "typographical symbol"
  ],
  "claims": {
   "P279": [
    "Q80071"
   ],
   "P361": [
    "Q159964",
    "Q234460",
    "Q184757"
   ],
   "P460": [
    "Q2372244"
   ],
   "P1889": [
    "Q32483",
    "Q29654788"
   ]
  },
  "revision_id": "2570039010",
  "ancestor_of": "Q263478",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q151411",
  "label": "designation",
  "description": "representation of a term by linguistic or other means",
  "aliases": [
   "naming",
   "labelling"
  ],
  "claims": {
   "P31": [
    "Q122754124"
   ],
   "P279": [
    "Q3695082",
    "Q1914636"
   ]
  },
  "revision_id": "2506596433",
  "ancestor_of": "Q263478",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q63539947",
  "label": "artistic concept",
  "description": "concept used in artistic practice",
  "aliases": [
   "art concept",
   "concept in art"
  ],
  "claims": {
   "P31": [
    "Q137429456"
   ],
   "P279": [
    "Q151885"
   ]
  },
  "revision_id": "2481116498",
  "ancestor_of": "Q263478",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q80071",
  "label": "symbol",
  "description": "something that represents an idea, a process, or a physical entity due to convention or association",
  "aliases": [
   "symbols",
   "Zsym"
  ],
  "claims": {
   "P279": [
    "Q3695082",
    "Q1272626",
    "Q151885",
    "Q141152439"
   ],
   "P361": [
    "Q2001982"
   ],
   "P460": [
    "Q3695082",
    "Q11634359"
   ]
  },
  "revision_id": "2567580812",
  "ancestor_of": "Q263478",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q122754124",
  "label": "ambiguous Wikidata item",
  "description": "Wikidata item that refers to any of several items, which should usually be treated with separate Wikidata items",
  "aliases": [
   "ambiguous item",
   "conflated entity",
   "conflated item",
   "ambiguous entity",
   "conflated Wikidata item",
   "Wikidata ambiguous item",
   "Wikidata conflated item",
   "hybrid item"
  ],
  "claims": {
   "P31": [
    "Q27949697"
   ],
   "P279": [
    "Q16222597"
   ],
   "P460": [
    "Q21484471"
   ],
   "P1889": [
    "Q106573263"
   ]
  },
  "revision_id": "2572670917",
  "ancestor_of": "Q263478",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q3695082",
  "label": "sign",
  "description": "semiotic concept; object, quality, event, or entity whose presence or occurrence indicates the probable presence or occurrence of something else; includes words, punctuation, expressions, gestures, notices, road signs, symbols, pictures, etc.",
  "aliases": [
   "indicator",
   "indication"
  ],
  "claims": {
   "P31": [
    "Q151885"
   ],
   "P279": [
    "Q488383"
   ],
   "P527": [
    "Q16136913"
   ],
   "P460": [
    "Q80071",
    "Q11801374",
    "Q262246"
   ],
   "P1889": [
    "Q11183785",
    "Q1211272"
   ]
  },
  "revision_id": "2558088343",
  "ancestor_of": "Q263478",
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
  "ancestor_of": "Q263478",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q12827391",
  "label": "minor mode",
  "description": "mode that has as its characteristic a minor third in the tonal system",
  "aliases": [],
  "claims": {
   "P31": [
    "Q937228",
    "Q151885",
    "Q11696608"
   ],
   "P279": [
    "Q192822"
   ],
   "P361": [
    "Q1439151"
   ],
   "P1889": [
    "Q184567",
    "Q2585587",
    "Q113031008"
   ]
  },
  "revision_id": "2549933938",
  "ancestor_of": "Q283749",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q192822",
  "label": "tonal system",
  "description": "arrangements of pitches or chords to induce a hierarchy of perceived relations, stabilities, and attractions",
  "aliases": [
   "music tonality",
   "musical tonality",
   "tonality"
  ],
  "claims": {
   "P31": [
    "Q115211517"
   ],
   "P279": [
    "Q731978"
   ]
  },
  "revision_id": "2570916616",
  "ancestor_of": "Q283749",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q937228",
  "label": "property",
  "description": "predominant feature that characterizes a being, a thing, a phenomenon, etc. and which differentiates one being from another, one thing from another",
  "aliases": [
   "attribute",
   "characteristic"
  ],
  "claims": {
   "P31": [
    "Q19478619",
    "Q714737"
   ],
   "P279": [
    "Q7048977"
   ],
   "P460": [
    "Q1207505",
    "Q758243"
   ],
   "P1889": [
    "Q3924032",
    "Q1400881",
    "Q18616576",
    "Q124711455",
    "Q141475451",
    "Q109674924"
   ]
  },
  "revision_id": "2571699360",
  "ancestor_of": "Q283749",
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
  "ancestor_of": "Q283749",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q11696608",
  "label": "element of music",
  "description": "characteristic, dimension, or element taken as a part or component of music",
  "aliases": [
   "elements of a musical work",
   "aspect of music"
  ],
  "claims": {
   "P31": [
    "Q115211517"
   ],
   "P279": [
    "Q21040055",
    "Q1277572"
   ],
   "P361": [
    "Q638"
   ]
  },
  "revision_id": "2527574871",
  "ancestor_of": "Q283749",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q115211517",
  "label": "musical concept",
  "description": "type of artistic concept",
  "aliases": [],
  "claims": {
   "P279": [
    "Q63539947"
   ]
  },
  "revision_id": "2541599296",
  "ancestor_of": "Q283749",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q731978",
  "label": "mode",
  "description": "each of the sequences ordered by the notes within an octave according to the different sequences of tones and semitones",
  "aliases": [
   "musical mode",
   "Lad"
  ],
  "claims": {
   "P31": [
    "Q115211517",
    "Q12812139"
   ],
   "P279": [
    "Q184421"
   ],
   "P361": [
    "Q164204"
   ],
   "P1889": [
    "Q6888090"
   ]
  },
  "revision_id": "2551264913",
  "ancestor_of": "Q283749",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 2 of 3: Angular (`fcadn3ihwg`)

~~~~text
Concept record:
{
 "id": "fcadn3ihwg",
 "preferred_name": "Angular",
 "kind": "framework",
 "broad_class": "skill",
 "variants": [],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "swlrwigph5",
  "name": "Angular CLI"
 },
 {
  "id": "mnlgauzi32",
  "name": "AngularJS"
 },
 {
  "id": "cex5ha398q",
  "name": "Design"
 },
 {
  "id": "ls6hrpynv0",
  "name": "Java"
 },
 {
  "id": "y37j4kl3jo",
  "name": "TypeScript"
 },
 {
  "id": "d4xxm6t88j",
  "name": "DevOps"
 },
 {
  "id": "twhbebct5l",
  "name": "HTML"
 },
 {
  "id": "pk7cebmtg6",
  "name": "Python"
 },
 {
  "id": "hjzieo2ohv",
  "name": "React"
 },
 {
  "id": "ss273uzint",
  "name": "Software testing"
 },
 {
  "id": "xe2d2jfa1r",
  "name": "Application programming interface"
 },
 {
  "id": "op6iieveb7",
  "name": "Bash"
 },
 {
  "id": "f0c784bzd2",
  "name": "ngAnimate"
 },
 {
  "id": "k87r3b7xk8",
  "name": "Bengali"
 },
 {
  "id": "ciqcmsfd1o",
  "name": "Hungarian"
 },
 {
  "id": "hupkg1mnsj",
  "name": "Aurelia"
 },
 {
  "id": "cxpxcuw3gh",
  "name": "Anaplan"
 },
 {
  "id": "b2291n6joq",
  "name": "Lingala"
 },
 {
  "id": "z199mo1bdd",
  "name": "Fula"
 },
 {
  "id": "vks1qiiz57",
  "name": "Ainu"
 },
 {
  "id": "w8wmeqph17",
  "name": "Manipuri"
 },
 {
  "id": "vphlc8dpfb",
  "name": "Mandarin"
 },
 {
  "id": "tsdlbd9gt0",
  "name": "English"
 },
 {
  "id": "hth5eczuzx",
  "name": "Gujarati"
 },
 {
  "id": "ztt7xizgr8",
  "name": "Scala"
 },
 {
  "id": "z09tq03hir",
  "name": "Analysis of variance"
 },
 {
  "id": "ynw7yrzobc",
  "name": "Benga"
 },
 {
  "id": "yk1fji8zbq",
  "name": "Associate of Arts in Art"
 },
 {
  "id": "xstca7bdbk",
  "name": "Amazon SageMaker"
 },
 {
  "id": "xayt8bhrdg",
  "name": "AI guardrails"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "maminkheneifar/jobinja-job-listings-26k@v1/Jobinja - Processed.csv:121",
  "source": "kaggle:maminkheneifar/jobinja-job-listings-26k (CC0: Public Domain), column Job Description",
  "text": "C#, Angular, Sql Server, C#, Angular, Sql Server"
 },
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:76",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: Chuyên Gia Kiến Trúc Ứng Dụng - Solution Architect - Khối Công Nghệ Thông Tin (2025TD942). [\"Angular\", \"Angular\", \"Angular\", \"Microservice\", \"Oracle\", \"Redis\", \"Spring\"]"
 },
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:148",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: L3 SAN Storage Engineer. …patterns affect storage (LUN Q-Depth, multipathing, application IO size, etc…). Development skill sets including: Python, Cloud frameworks, Angular, and a mindset for automation is a plus."
 },
 {
  "id": "mohityd2007/real-world-job-postings-dataset-for-ml-projects@v1/jobs_data.csv:4585",
  "source": "kaggle:mohityd2007/real-world-job-postings-dataset-for-ml-projects (Attribution 4.0 International (CC BY 4.0)), column Job Description",
  "text": "Job title: Java Developer. Key Responsibilities: 1. Develop and maintain high-quality software solutions using Java, Spring MVC, Hibernate, Angular 7.0, and MySQL. 2. Collaborate with cross-functional teams to design, develop, and test software applications. 3. Participate in code reviews and provide constructive feedback to …"
 },
 {
  "id": "q1n9huan/global-job-market-postings-dataset@v1/foreign_jobs.release_candidate_v14_enriched.kaggle.csv:15",
  "source": "kaggle:q1n9huan/global-job-market-postings-dataset (CC0: Public Domain), column description",
  "text": "Job title: Senior DevOps Engineer. devops|.net|android|aws|azure|c|c#|c++|data science|golang|ios|java|javascript|kubernetes|node.js|php|python|react|ruby/rails|scala|shopify|sql|swift|ui/ux|wordpress|blockchain|ai/ml|automation|project management|react native|rust|product management|unity|electron|spring|data analysis|bash|laravel|e…"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[
 {
  "title": "Angular (web framework)",
  "revision_id": "1375216833",
  "matched_by": "title-minus-qualifier",
  "text": "Angular (also referred to as Angular 2+) is a TypeScript-based free and open-source single-page web application framework. It is developed by Google and by a community of individuals and corporations. Angular is a complete rewrite from the same team that built AngularJS. The Angular ecosystem consists of a diverse group of over 1.7 million developers, library authors, and content creators. According to the Stack Overflow Developer Survey, Angular is one of the most commonly used web frameworks.\n\nDifferences between Angular and AngularJS\n\nGoogle designed Angular as a ground-up rewrite of AngularJS. Unlike AngularJS, Angular does not have a concept of \"scope\" or controllers; instead, it uses a hierarchy of components as its primary architectural characteristic. Angular has a different expression syntax, focusing on \"[ ]\" for property binding, and \"( )\" for event binding. Angular recommends the use of Microsoft's TypeScript language, which introduces features such as static typing, generics, and type annotations.\n\nFeatures\n\nComponent-based architecture\n\nAngular uses a component-based architecture, which allows developers to build encapsulated, reusable user interface elements. Each component encapsulates its own HTML, CSS, and TypeScript, making it easier to manage and test individual pieces of an application.\n\nData binding\n\nAngular supports two-way data binding which synchronizes data between the model and the view. This ensures that any changes in the view are automatically reflected in the model and vice versa.\n\nDependency injection\n\nAngular has a built-in dependency injection system that makes it easier to manage and inject dependencies into components and services. This promotes modularity and easier testing.\n\nDirectives\n\nAngular extends HTML with additional attributes called directives. Directives offer functionality to change the behavior or appearance of DOM elements.\n\nRouting\n\nAngular includes a router that allows developers to define and manage application states and navigation paths, making it easier to build single-page applications with complex routing.\n\nAngular CLI\n\nThe Angular CLI (Command Line Interface) provides a set of tools for creating, building, testing, and deploying Angular applications. It enables rapid application setup and simplifies ongoing development tasks.\n\nServer-side rendering\n\nAngular has official support for server-side rendering, which improves an application's load time and performance. Server-side rendering also enhances search engine optimization by making content more accessible to web crawlers.\n\nHistory\n\nAngular 2.0 was announced during the keynote of the 2014 NG-Conf conference 16–17 January 2014. On April 30, 2015, the Angular developers announced that Angular 2 moved from Alpha to Developer Preview. Angular 2 moved to Beta in December 2015, and the first release candidate was published in May 2016. The final version was released on 14 September 2016.\n\nVersion 8 of Angular introduced a new compilation and rendering pipeline, Ivy, and version 9 of Angular enabled Ivy by default. Angular 13 removed the deprecated former compiler, View Engine. Angular 14 introduced standalone components and Angular 17 made them the default, de-emphasizing the use of modules.\n\nAngular 18, released in 2024, introduced several improvements such as standalone components defaulting to true, built-in control flow syntax, zoneless support previews, and modern SSR debugging tools.\n\nNaming\n\nThe rewrite of AngularJS was called \"Angular 2\", but this led to confusion among developers. To clarify, the team announced that separate names should be used for each framework with \"AngularJS\" referring to the 1.X versions and \"Angular\" without the \"JS\" referring to versions 2 and up.\n\nVersion history\n\nFuture releases\n\nSince v9, the Angular team has moved all new applications to use the Ivy compiler and runtime. They will be working on Ivy to improve output bundle sizes and development speeds.\n\nEach version is expected to be backward-compatible with the prior release, yet it is still challenging. The Angular development team has pledged to do twice-a-year upgrades.\n\nSupport policy and schedule\n\nAll the major releases are supported for 24 months. This consists of 12 months of active support, during which regularly scheduled updates and patches are released. It is then followed by 12 months of long-term support (LTS), during which only critical fixes and security patches are released.\n\nAngular versions v2 to v19 are no longer under support.\n\nAssociated projects\n\nAnalog is a full stack web meta-framework based upon Angular powered by Vite and Nitro.\n\nLibraries\n\nAngular Material\n\nAngular Material is a UI component library that implements Material Design in Angular. It provides a collection of reusable components that adhere to Google's Material Design specifications, aiming to offer a consistent user interface across different devices and platforms.\n\nAngular Material includes a variety of UI components such as buttons, cards, dialogs, grids, and form controls. These components are designed to be customizable and easy to integrate into Angular applications. Additional features of Angular Material include support for responsive design, theming, and accessibility.\n\nAngular Elements\n\nIn 2018, Angular 6 introduced Angular Elements, enabling developers to package Angular components as custom web elements, which are part of the web components set of web platform APIs.\n\nSee also"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q28925578",
  "label": "Angular",
  "description": "web application framework",
  "aliases": [
   "Angular 2+"
  ],
  "claims": {
   "P31": [
    "Q341",
    "Q1330336"
   ]
  },
  "revision_id": "2528046131",
  "value_labels": {
   "Q341": "free software",
   "Q1330336": "web framework"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q341",
  "label": "free software",
  "description": "software distributed under terms that allow users to freely run, study, change and distribute it and modified versions",
  "aliases": [
   "libre software",
   "Free Software"
  ],
  "claims": {
   "P31": [
    "Q17155032"
   ],
   "P279": [
    "Q5500964",
    "Q56273712",
    "Q1130645"
   ],
   "P361": [
    "Q1076638"
   ],
   "P460": [
    "Q1130645",
    "Q506883"
   ],
   "P1889": [
    "Q178285",
    "Q5500964",
    "Q1130645",
    "Q3943414"
   ]
  },
  "revision_id": "2572795734",
  "ancestor_of": "Q28925578",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1330336",
  "label": "web framework",
  "description": "software framework that is designed to support the development of websites, web applications, web services and web resources",
  "aliases": [
   "web application framework",
   "WAF"
  ],
  "claims": {
   "P279": [
    "Q271680"
   ]
  },
  "revision_id": "2546719697",
  "ancestor_of": "Q28925578",
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
  "ancestor_of": "Q28925578",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q5500964",
  "label": "freely redistributable software",
  "description": "software that anyone is free to redistribute",
  "aliases": [
   "FRS"
  ],
  "claims": {
   "P279": [
    "Q7397"
   ],
   "P1889": [
    "Q178285",
    "Q341",
    "Q7048868"
   ]
  },
  "revision_id": "2549515023",
  "ancestor_of": "Q28925578",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q56273712",
  "label": "source-available software",
  "description": "software distributed with its source code",
  "aliases": [],
  "claims": {
   "P279": [
    "Q7397"
   ],
   "P1889": [
    "Q506883",
    "Q1130645"
   ]
  },
  "revision_id": "2550276284",
  "ancestor_of": "Q28925578",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1130645",
  "label": "open-source software",
  "description": "software that anyone is free to use and redistribute in its current state with a permissive licence giving a libre access to its original source code (but not necessarily to modify it)",
  "aliases": [
   "open source software",
   "open-source code software",
   "OSS"
  ],
  "claims": {
   "P279": [
    "Q56273712",
    "Q5500964",
    "Q1293664"
   ],
   "P361": [
    "Q2251455"
   ],
   "P460": [
    "Q341",
    "Q506883"
   ],
   "P1889": [
    "Q39162",
    "Q341",
    "Q1156659",
    "Q506883",
    "Q56273712"
   ]
  },
  "revision_id": "2572055300",
  "ancestor_of": "Q28925578",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q271680",
  "label": "software framework",
  "description": "software that supports solution development via inversion of control",
  "aliases": [
   "framework",
   "software platform",
   "computational framework"
  ],
  "claims": {
   "P31": [
    "Q17155032"
   ],
   "P279": [
    "Q40056",
    "Q15411548",
    "Q241317",
    "Q188860"
   ],
   "P460": [
    "Q188860"
   ]
  },
  "revision_id": "2523831113",
  "ancestor_of": "Q28925578",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 3 of 3: AngularJS (`mnlgauzi32`)

~~~~text
Concept record:
{
 "id": "mnlgauzi32",
 "preferred_name": "AngularJS",
 "kind": "framework",
 "broad_class": "skill",
 "variants": [
  {
   "label": "Angular.js"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "fcadn3ihwg",
  "name": "Angular"
 },
 {
  "id": "twhbebct5l",
  "name": "HTML"
 },
 {
  "id": "h60l8olauw",
  "name": "JavaScript"
 },
 {
  "id": "bzg3r9ulfm",
  "name": "BIND"
 },
 {
  "id": "cex5ha398q",
  "name": "Design"
 },
 {
  "id": "l54jfkzunm",
  "name": "Programming"
 },
 {
  "id": "y37j4kl3jo",
  "name": "TypeScript"
 },
 {
  "id": "oxu0hc83pv",
  "name": "Computer science"
 },
 {
  "id": "x4397709dt",
  "name": "CSS"
 },
 {
  "id": "pl9ucmohz5",
  "name": "Express.js"
 },
 {
  "id": "q89d2f20gq",
  "name": "Node.js"
 },
 {
  "id": "hjzieo2ohv",
  "name": "React"
 },
 {
  "id": "ojeubzzg6x",
  "name": "Gulp.js"
 },
 {
  "id": "swlrwigph5",
  "name": "Angular CLI"
 },
 {
  "id": "v4wdughw0p",
  "name": "Handlebars.js"
 },
 {
  "id": "k87r3b7xk8",
  "name": "Bengali"
 },
 {
  "id": "d868fdr68x",
  "name": "Scala.js"
 },
 {
  "id": "rnblhw89i9",
  "name": "CanvasJS"
 },
 {
  "id": "f0mg2qvhta",
  "name": "Nuxt"
 },
 {
  "id": "cf2acgxwct",
  "name": "MEAN.JS"
 },
 {
  "id": "f0c784bzd2",
  "name": "ngAnimate"
 },
 {
  "id": "vjw6nn9z7a",
  "name": "CanJS"
 },
 {
  "id": "v00xfjkjpc",
  "name": "Chart.js"
 },
 {
  "id": "hxclrzb8sy",
  "name": "Bacon.js"
 },
 {
  "id": "cvjjttyqe3",
  "name": "Sails.js"
 },
 {
  "id": "xayt8bhrdg",
  "name": "AI guardrails"
 },
 {
  "id": "xwrfu2zstu",
  "name": "NW.js"
 },
 {
  "id": "p98xjhlkpu",
  "name": "Ingres"
 },
 {
  "id": "n3e2gcdwp6",
  "name": "pandas"
 },
 {
  "id": "ciqcmsfd1o",
  "name": "Hungarian"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:963",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: .NET Full Stack Developer. [\"ReactJS\", \"Full Stack Development\", \"C#\", \"AngularJS\", \".NET\"]"
 },
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:229",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Big Data Software Engineer. … CentOS, installing, troubleshooting and command-line scripting. Knowledge of restful APIs (creating and consuming) is helpful Knowledge of AngularJS, jQuery, nodeJS is helpful Desire to learn existing and new technologies around the Big Data space Responsibilities Selecting and integrating any Big …"
 },
 {
  "id": "dev122/internshala-jobs-dataset@v1/JobData.csv:11",
  "source": "kaggle:dev122/internshala-jobs-dataset (CC0: Public Domain), column Description",
  "text": "Job title: Angular.js Development Intern (Remote). … day-to-day responsibilities include: 1. Collaborate with the development team to design and implement user-friendly web applications using AngularJS, HTML, CSS, and Redux 2. Write clean, maintainable, and efficient code 3. Utilize Redux for state management within AngularJS applications 4. Develop …"
 },
 {
  "id": "mohityd2007/real-world-job-postings-dataset-for-ml-projects@v1/jobs_data.csv:4872",
  "source": "kaggle:mohityd2007/real-world-job-postings-dataset-for-ml-projects (Attribution 4.0 International (CC BY 4.0)), column Job Description",
  "text": "Job title: Full Stack Developer. .NET,MongoDB,AngularJS,Node.js,PostgreSQL,Express.js,React,"
 },
 {
  "id": "maminkheneifar/jobinja-job-listings-26k@v1/Jobinja - Processed.csv:11856",
  "source": "kaggle:maminkheneifar/jobinja-job-listings-26k (CC0: Public Domain), column Job Description",
  "text": ".NET Core, AngularJS, typescript, OOP, Object Oriented, MVC, webservice, SQL"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[
 {
  "title": "AngularJS",
  "revision_id": "1350503098",
  "matched_by": "title",
  "text": "AngularJS (also known as Angular 1) is a discontinued free and open-source JavaScript-based web framework for developing single-page applications. It was maintained mainly by Google and a community of individuals and corporations. It aimed to simplify both the development and the testing of such applications by providing a framework for client-side model–view–controller (MVC) and model–view–viewmodel (MVVM) architectures, along with components commonly used in web applications and progressive web applications.\n\nAngularJS was used as the frontend of the MEAN stack, that consisted of MongoDB database, Express.js web application server framework, AngularJS itself (or Angular), and Node.js server runtime environment.\n\nAs of January 1, 2022, Google no longer updates AngularJS to fix security, browser compatibility, or jQuery issues. The Angular team recommends upgrading to Angular (v2+) as the best path forward, but they also provided some other options.\n\nOverview\n\nThe AngularJS framework worked by first reading the HyperText Markup Language (HTML) page, which had additional custom HTML attributes embedded into it. Angular interpreted those attributes as directives to bind input or output parts of the page to a model that is represented by standard JavaScript variables. The values of those JavaScript variables could be manually set within the code or retrieved from static or dynamic JSON resources.\n\nAngularJS was built on the belief that declarative programming should be used to create user interfaces and connect software components, while imperative programming was better suited to defining an application's business logic. The framework adapted and extended traditional HTML to present dynamic content through two-way data-binding that allowed for the automatic synchronization of models and views. As a result, AngularJS de-emphasized explicit Document Object Model (DOM) manipulation with the goal of improving testability and performance.\n\nAngularJS's design goals included:\n\nto decouple DOM manipulation from application logic. The difficulty of this is dramatically affected by the way the code is structured.\n\nto decouple the client side of an application from the server-side. This allows development work to progress in parallel and allows for reuse of both sides.\n\nto provide structure for the journey of building an application: from designing the UI, through writing the business logic, to testing.\n\nAngularJS implemented the MVC pattern to separate presentation, data, and logic components. Using dependency injection, Angular brought traditionally server-side services, such as view-dependent controllers, to client-side web applications. Consequently, much of the burden on the server could be reduced.\n\nScope\n\nAngularJS used the term \"scope\" in a manner akin to the fundamentals of computer science.\n\nScope in computer science describes when in the program a particular binding is valid. The ECMA-262 specification defines scope as: a lexical environment in which a Function object is executed in client-side web scripts; akin to how scope is defined in lambda calculus.\n\nAs a part of the \"MVC\" architecture, the scope forms the \"Model\", and all variables defined in the scope can be accessed by the \"View\" as well as the \"Controller\". The scope behaves as a glue and binds the \"View\" and the \"Controller\".\n\nBootstrap\n\nThe task performed by the AngularJS bootstrapper occurred in three phases after the DOM has been loaded:\n\nCreation of a new Injector\n\nCompilation of the directives that decorate the DOM\n\nLinking of all directives to scope\n\nAngularJS directives allowed the developer to specify custom and reusable HTML-like elements and attributes that define data bindings and the behavior of presentation components. Some of the most commonly used directives were:\n\nng-animate\n\nA module provides support for JavaScript, CSS3 transition and CSS3 keyframe animation hooks within existing core and custom directives.\nng-app\n\nDeclares the root element of an AngularJS application, under which directives can be used to declare bindings and define behavior.\nng-aria\n\nA module for accessibility support of common ARIA attributes.\nng-bind\n\nSets the text of a DOM element to the value of an expression. For example, <span ng-bind=\"name\"></span> displays the value of 'name' inside the span element. Any change to the variable 'name' in the application's scope reflect instantly in the DOM.\nng-class\n\nConditionally apply a class, depending on the value of a Boolean expression.\nng-controller\n\nSpecifies a JavaScript controller class that evaluates HTML expressions.\nng-if\n\nBasic if statement directive that instantiates the following element if the conditions are true. When the condition is false, the element is removed from the DOM. When true, a clone of the compiled element is re-inserted.\nng-init\n\nCalled once when the element is initialized.\nng-model\n\nSimilar to ng-bind, but establishes a two-way data binding between the view and the scope.\nng-model-options\n\nProvides tuning for how model updates are done.\nng-repeat\n\nInstantiate an element once per item from a collection.\nng-show & ng-hide\n\nConditionally show or hide an element, depending on the value of a Boolean expression. Show and hide is achieved by setting the CSS display style.\nng-switch\n\nConditionally instantiate one template from a set of choices, depending on the value of a selection expression.\nng-view\n\nThe base directive responsible for handling routes that resolve JSON before rendering templates driven by specified controllers.\n\nSince ng-* attributes are not valid in HTML specifications, data-ng-* can also be used as a prefix. For example, both ng-app and data-ng-app are valid in AngularJS.\n\nTwo-way data binding\n\nAngularJS two-way data binding had its most notable feature, largely relieving the server backend of templating responsibilities. Instead, templates were rendered in plain HTML according to data contained in a scope defined in the model. The $scope service in Angular detected changes to the model section and modified HTML expressions in the view via a controller. Likewise, any alterations to the view were reflected in the model. This circumvented the need to actively manipulate the DOM and encouraged bootstrapping and rapid prototyping of web applications.\nAngularJS detected changes in models by comparing the current values with values stored earlier in a process of dirty-checking, unlike Ember.js and Backbone.js that triggered listeners when the model values are changed.\n\n$watch\n\nis an angular method used for dirty checking. Any variable or expression assigned in $scope automatically sets up a $watchExpression in angular. So assigning a variable to $scope or using directives like ng-if, ng-show, ng-repeat etc. all create watches in angular scope automatically. Angular maintains a simple array of $$watchers in the $scope objects\n\nDifferent ways of defining a watcher in AngularJS.\n\nexplicitly $watch an attribute on $scope.\n\n$scope.$watch('person.username', validateUnique);\n\nplace an interpolation in your template (a watcher will be created for you on the current $scope).\n\nask a directive such as ng-model to define the watcher for you.\n\n<input ng-model=\"person.username\" />\n$digest\n\nis angular method that is invoked internally by angularjs in frequent intervals. In $digest method, angular iterates over all $watches in its scope/child scopes.\n$apply\n\nis an angular method that internally invokes $digest. This method is used when you want to tell angular manually start dirty checking (execute all $watches)\n$destroy\n\nis both a method and event in angularjs. $destroy() method, removes a scope and all its children from dirty checking. $destroy event is called by angular whenever a $scope or $controller is destroyed.\n\nDevelopment history\n\nAngularJS was originally developed in 2009 by Miško Hevery at Brat Tech LLC as the software behind an online JSON storage service, that would have been priced by the megabyte, for easy-to-make applications for the enterprise. This venture was located at the web domain \"GetAngular.com\", and had a few subscribers, before the two decided to abandon the business idea and release Angular as an open-source library.\n\nThe 1.6 release added many of the concepts of Angular to AngularJS, including the concept of a component-based application architecture. This release among others removed the Sandbox, which many developers believed provided additional security, despite numerous vulnerabilities that had been discovered that bypassed the sandbox. The current (as of November 2023) stable release of AngularJS is 1.8.3\n\nIn January 2018, a schedule was announced for phasing-out AngularJS: after releasing 1.7.0, the active development on AngularJS would continue until June 30, 2018. Afterwards, 1.7 was supported until December 31, 2021 as long-term support.\n\nLegacy browser support\n\nVersions 1.3 and later of AngularJS did not support Internet Explorer 8 or earlier. While AngularJS 1.2 supported IE8, its team does not.\n\nAngular and AngularDart\n\nSubsequent versions of AngularJS are simply called Angular. Angular is an incompatible TypeScript-based rewrite of AngularJS. Angular 4 was announced on 13 December 2016, skipping 3 to avoid a confusion due to the misalignment of the router package's version which was already distributed as v3.3.0.\n\nAngularDart works on Dart, which is an object-oriented, class-based, and single inheritance programming language using C-style syntax. This differs from AngularJS (which uses JavaScript) and later versions of Angular such as Angular 2 and Angular 4 (which use TypeScript). Angular 4 was released in March 2017, with the framework's version aligned with the version number of the router it used. Angular 5 was released on November 1, 2017. Key improvements in Angular 5 include support for progressive web applications, a build optimizer, and enhancements related to Material Design. Angular 6 was released on May 3, 2018, followed by Angular 7 on October 18, 2018, and Angular 8 on May 28, 2019.\n\nAngular follows Semantic Versioning standards, with each major version number indicating potentially breaking changes. Angular has pledged to provide 6 months of active support for each major version followed by 12 months of long-term support. Major releases are bi-yearly with 1 to 3 minor releases for every major release.\n\nAngular Universal\n\nA normal Angular application executes in the browser, while Angular Universal generates static application pages on the server through server-side rendering (SSR).\n\nLibraries\n\nAngularJS Material\n\nAngularJS Material was a UI component library that implemented Material Design in AngularJS. The library provided a set of reusable, well-tested, and accessible UI components. In January 2022, the library was closed, as announced on their official website. The AngularJS Material library is a mature and stable product that is ready for production use and works only with AngularJS 1.x. The Angular Material library is available in the angular/material2 GitHub repository.\n\nChrome extension\n\nIn July 2012, the Angular team built an extension for the Google Chrome browser called Batarang, that improved the debugging experience for web applications built with Angular. The extension aimed to allow for easy detection of performance bottlenecks and offered a GUI for debugging applications. For a time during late 2014 and early 2015, the extension was not compatible with recent releases (after v1.2.x) of Angular. The last update made to this extension was on April 4, 2017. Additionally, the extension was removed from the Chrome Web Store on June 1, 2022, due to its lack of updates and potential security concerns, such as requiring sensitive permissions.\n\nPerformance\n\nAngularJS set out the paradigm of a digest cycle. This cycle could be considered a loop, during which AngularJS checked if there were any changes to all the variables watched by all the $scopes. If $scope.myVar is defined in a controller and this variable was marked for watching, Angular would monitor the changes on myVar in each loop iteration.\n\nThis approach potentially led to slow rendering when AngularJS checked on too many variables in the $scope every cycle. Miško Hevery suggested keeping fewer than 2000 watchers on any page.\n\nSee also"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q2849803",
  "label": "AngularJS",
  "description": "open source web application framework",
  "aliases": [
   "Angular.js",
   "Angular JS",
   "Angular 1."
  ],
  "claims": {
   "P31": [
    "Q271680",
    "Q783866",
    "Q188860"
   ]
  },
  "revision_id": "2550169984",
  "value_labels": {
   "Q271680": "software framework",
   "Q783866": "JavaScript library",
   "Q188860": "software library"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q271680",
  "label": "software framework",
  "description": "software that supports solution development via inversion of control",
  "aliases": [
   "framework",
   "software platform",
   "computational framework"
  ],
  "claims": {
   "P31": [
    "Q17155032"
   ],
   "P279": [
    "Q40056",
    "Q15411548",
    "Q241317",
    "Q188860"
   ],
   "P460": [
    "Q188860"
   ]
  },
  "revision_id": "2523831113",
  "ancestor_of": "Q2849803",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q783866",
  "label": "JavaScript library",
  "description": "library of JavaScript code that allows for easier development of JavaScript-based applications",
  "aliases": [
   "JS library",
   "JS lib"
  ],
  "claims": {
   "P31": [
    "Q17155032"
   ],
   "P279": [
    "Q188860"
   ]
  },
  "revision_id": "2517019784",
  "ancestor_of": "Q2849803",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q188860",
  "label": "software library",
  "description": "collection of non-volatile resources used by computer programs, often for software development",
  "aliases": [
   "programming library",
   "lib",
   "library",
   "code generation library",
   "computer library"
  ],
  "claims": {
   "P31": [
    "Q17155032"
   ],
   "P279": [
    "Q1077784",
    "Q17176533",
    "Q7397"
   ],
   "P361": [
    "Q1995545"
   ],
   "P460": [
    "Q126008353"
   ],
   "P1889": [
    "Q7075"
   ]
  },
  "revision_id": "2560237477",
  "ancestor_of": "Q2849803",
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
  "ancestor_of": "Q2849803",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q40056",
  "label": "computer program",
  "description": "sequence of instructions written in programming language to perform a specified task with a computer",
  "aliases": [
   "program",
   "software program"
  ],
  "claims": {
   "P279": [
    "Q4303335",
    "Q11491547",
    "Q141543245"
   ],
   "P361": [
    "Q1143070",
    "Q7397",
    "Q56822593"
   ],
   "P1889": [
    "Q205663"
   ]
  },
  "revision_id": "2565022818",
  "ancestor_of": "Q2849803",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q15411548",
  "label": "computing infrastructure",
  "description": "",
  "aliases": [],
  "claims": {
   "P31": [
    "Q131339603"
   ],
   "P279": [
    "Q121359"
   ]
  },
  "revision_id": "2528012860",
  "ancestor_of": "Q2849803",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q241317",
  "label": "computing platform",
  "description": "environment in which a piece of software is executed",
  "aliases": [
   "platform",
   "digital platform",
   "computing environment",
   "app layer",
   "execution environment"
  ],
  "claims": {
   "P279": [
    "Q2424752",
    "Q994895"
   ]
  },
  "revision_id": "2552001373",
  "ancestor_of": "Q2849803",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1077784",
  "label": "programming tool",
  "description": "computer program that software developers use to support other programs and applications",
  "aliases": [
   "software development tool",
   "development tool",
   "computer programming tool",
   "application programming tool",
   "developer tool",
   "programmer tool"
  ],
  "claims": {
   "P31": [
    "Q17155032",
    "Q123588392"
   ],
   "P279": [
    "Q312466"
   ]
  },
  "revision_id": "2527989107",
  "ancestor_of": "Q2849803",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q17176533",
  "label": "software component",
  "description": "software package, web service, web resource, or module that encapsulates a set of related functions",
  "aliases": [
   "component",
   "software componentry",
   "app feature",
   "website feature",
   "website part",
   "app part"
  ],
  "claims": {
   "P279": [
    "Q66310127",
    "Q110832782"
   ],
   "P361": [
    "Q40056"
   ]
  },
  "revision_id": "2565979938",
  "ancestor_of": "Q2849803",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q7397",
  "label": "software",
  "description": "non-tangible executable component of a computer",
  "aliases": [
   "computer software",
   "computational tool",
   "dghed",
   "SW"
  ],
  "claims": {
   "P31": [
    "Q63981612",
    "Q123588392"
   ],
   "P279": [
    "Q17537576",
    "Q47461344",
    "Q12774177",
    "Q2424752"
   ],
   "P361": [
    "Q68",
    "Q1194864"
   ],
   "P527": [
    "Q40056",
    "Q494756"
   ],
   "P1889": [
    "Q2297604",
    "Q104851"
   ]
  },
  "revision_id": "2570277370",
  "ancestor_of": "Q2849803",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~
