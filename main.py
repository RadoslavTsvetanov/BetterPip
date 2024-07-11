
        <header class="navbar hide-xs">
    <section class="navbar-section">
        <h2><a href="/" class="title-navbar">crackmes.one</a></h2>
    </section>
    <section class="navbar-center">
        -
    </section>

    

<section class="navbar-section">
    <a href="/search" class="btn btn-link">Search</a>
    <a href="/lasts/1" class="btn btn-link">Latest Crackmes</a>
    <a href="/faq" class="btn btn-link">Faq</a>
    <a href="/login" class="btn btn-link">Login</a>
    <a href="/register" class="btn btn-link">Register</a>
</section>
</header>
<div class="off-canvas show-xs">
    <h2 class="text-center"><a href="/" class="title-navbar">crackmes.one</a></h2>
    
    <a class="off-canvas-toggle btn btn-primary btn-action" href="#sidebar-id">
        <i class="icon icon-menu"></i>
    </a>

    <div id="sidebar-id" class="off-canvas-sidebar">
        <ul class="nav">
            <li class="nav"><a href="/search" class="btn btn-link">Search</a>
            </li><li class="nav"><a href="/lasts/1" class="btn btn-link">Latest Crackmes</a></li>
            <li class="nav"><a href="/faq" class="btn btn-link">Faq</a></li>
            <li class="nav"><a href="/login" class="btn btn-link">Login</a></li>
            <li class="nav"><a href="/register" class="btn btn-link">Register</a></li>
        </ul>
    </div>
    <a class="off-canvas-overlay" href="#close"></a>
    
</div>


        
        


<div class="container grid-lg wrapper">

    <h2>Crackme search</h2>
    <form class="form-horizontal" method="post">
        <div class="form-group">
            <div class="col-3">Crackme name</div>
            <div class="col-9 col-sm-12">
                <input class="form-input" type="text" id="name" name="name" placeholder="Name">
            </div> 
        </div>
        <div class="form-group">
            <div class="col-3">Author</div>
            <div class="col-9 col-sm-12">
                <input class="form-input" type="text" id="author" name="author" placeholder="Author">
            </div>
        </div>
        <div class="form-group">
            <div class="col-3 col-sm-12">
                <label class="form-label">Difficulty between</label>
            </div>
            <div class="col-9 col-sm-12">
                <select class="form-select" id="difficulty-min" name="difficulty-min" style="max-width: 20%">
                    <option selected="selected" value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                    <option value="6">6</option>
                </select>
                and 
                <select class="form-select" id="difficulty-max" name="difficulty-max" style="max-width: 20%">
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                    <option selected="selected" value="6">6</option>
                </select>
            </div>
        </div>
        <div class="form-group">
            <div class="col-3 col-sm-12">
                <label class="form-label">Quality between</label>
            </div>
            <div class="col-9 col-sm-12">
                <select class="form-select" id="quality-min" name="quality-min" style="max-width: 20%">
                    <option selected="selected" value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                    <option value="6">6</option>
                </select>
                and 
                <select class="form-select" id="quality-max" name="quality-max" style="max-width: 20%">
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                    <option selected="selected" value="6">6</option>
                </select>
            </div>
        </div>
        <div class="form-group">
            <div class="col-3 col-sm-12">
                <label class="form-label" for="lang">Langage</label>
            </div>
            <div class="col-9 col-sm-12">
                <select class="form-select" id="lang" name="lang" multiple="">
                    <option value="C/C++">C/C++</option>
                    <option value="Assembler">Assembler</option>
                    <option value="Java">Java</option>
                    <option value="\(Visual\) Basic">(Visual) Basic</option>
                    <option value="Borland Delphi">Borland Delphi</option>
                    <option value="Turbo Pascal">Turbo Pascal</option>
                    <option value="\.NET">.NET</option>
                    <option value="Unspecified/other">Unspecified/other</option>
                </select>
            </div>
        </div>
        <div class="form-group">
            <div class="col-3 col-sm-12">
                <label class="form-label" for="arch">Arch</label>
            </div>
            <div class="col-9 col-sm-12">
                <select class="form-select" id="arch" name="arch" multiple="">
                    <option value="x86">x86</option>
                    <option value="x86-64">x86-64</option>
                    <option value="java">java</option>
                    <option value="ARM">ARM</option>
                    <option value="MIPS">MIPS</option>
                    <option value="other">other</option>
                </select>
            </div>
        </div>
        <div class="form-group">
            <div class="col-3 col-sm-12">
                <label class="form-label" for="platform">Platform</label>
            </div>
            <div class="col-9 col-sm-12">
                <select class="form-select" id="platform" name="platform" multiple="">
                    <option value="DOS">DOS</option> 
                    <option value="Mac OS X">Mac OS X</option>
                    <option value="Multiplatform">Multiplatform</option> 
                    <option value="Unix/linux etc\.">Unix/linux etc.</option>
                    <option value="Windows">Windows</option>
                    <option value="Windows 2000/XP only">Windows 2000/XP only</option>
                    <option value="Windows 7 Only">Windows 7 Only</option>
                    <option value="Windows Vista Only">Windows Vista Only</option>
                    <option value="Unspecified/other">Unspecified/other</option>
                </select>
            </div>
        </div>
        <input type="submit" class="btn active float-right" value="Search"> 
        <input type="hidden" id="token" name="token" value="H7fYrFs0BkS59d5ug6RvlXrVfvZ1jVX7">
    </form>
    <table class="table table-striped">
        <thead>
            <tr style="text-align: center;">
                <th style="width: 20%;">Name</th>
                <th style="width: 20%;">Author</th>
                <th style="width: 9%;">Language</th>
                <th style="width: 9%;">Arch</th>
                <th style="width: 4%;">Difficulty</th>
                <th style="width: 4%;">Quality</th>
                <th style="width: 9%;">Platform</th>
                <th style="width: 9%;">Date</th>
                <th style="width: 4%;">Solution</th>
                <th style="width: 4%;">Comments</th>
            </tr>
        </thead>
        <tbody id="content-list">
            
            <tr class="text-center">
                <td> <a href="/crackme/66736380e7b35c09bb266f92">baby's first crackme</a></td>
                <td> <a href="/user/mystic_rust">mystic_rust</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 11:02 PM 06/19/2024 </td>
                <td> 0 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/6672bf9ee7b35c09bb266f5e">KGenMe v2</a></td>
                <td> <a href="/user/dzonerzy">dzonerzy</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 11:23 AM 06/19/2024 </td>
                <td> 0 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/6640d1d26b8bd8ddfe33c80a">guess_the_password</a></td>
                <td> <a href="/user/b4te">b4te</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.1 </td>
                <td> 3.6 </td>
                <td> Unix/linux etc. </td>
                <td> 2:27 PM 05/12/2024 </td>
                <td> 1 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/6629bf7aa562ef06c3b52e86">Crack On The Cob - COBOL</a></td>
                <td> <a href="/user/froglover22">froglover22</a> </td>
                <td> Unspecified/other </td>
                <td> x86-64 </td>
                <td> 1.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 2:27 AM 04/25/2024 </td>
                <td> 1 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/66299081a562ef06c3b52e76">Find the Flag</a></td>
                <td> <a href="/user/froglover22">froglover22</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.5 </td>
                <td> Unix/linux etc. </td>
                <td> 11:06 PM 04/24/2024 </td>
                <td> 2 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/6617d3a5cddae72ae250c556">Authorize by PIN</a></td>
                <td> <a href="/user/AnanasCharles">AnanasCharles</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.9 </td>
                <td> 4.4 </td>
                <td> Unix/linux etc. </td>
                <td> 12:12 PM 04/11/2024 </td>
                <td> 2 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/660a24f1cddae72ae250bf56">Getting started</a></td>
                <td> <a href="/user/stonezarcon">stonezarcon</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.6 </td>
                <td> 4.6 </td>
                <td> Unix/linux etc. </td>
                <td> 3:07 AM 04/01/2024 </td>
                <td> 4 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/65da0fce6d3d2b1fef4be4df">level2</a></td>
                <td> <a href="/user/nimacpp">nimacpp</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.2 </td>
                <td> 3.0 </td>
                <td> Unix/linux etc. </td>
                <td> 3:48 PM 02/24/2024 </td>
                <td> 4 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/65c926c6eef082e477ff6b5a">Password</a></td>
                <td> <a href="/user/Oxymore">Oxymore</a> </td>
                <td> Unspecified/other </td>
                <td> x86-64 </td>
                <td> 1.2 </td>
                <td> 2.2 </td>
                <td> Unix/linux etc. </td>
                <td> 7:57 PM 02/11/2024 </td>
                <td> 1 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/65c795a3eef082e477ff6a7e">sh0uld_b3_e4zy</a></td>
                <td> <a href="/user/cycrusader">cycrusader</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.3 </td>
                <td> 1.7 </td>
                <td> Unix/linux etc. </td>
                <td> 3:26 PM 02/10/2024 </td>
                <td> 0 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/65afe04ceef082e477ff6026">silly</a></td>
                <td> <a href="/user/Teknikclel69">Teknikclel69</a> </td>
                <td> Assembler </td>
                <td> x86 </td>
                <td> 1.4 </td>
                <td> 4.8 </td>
                <td> Unix/linux etc. </td>
                <td> 3:50 PM 01/23/2024 </td>
                <td> 2 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/65a172f0eef082e477ff5a6e">H1dd4n Fl4g</a></td>
                <td> <a href="/user/M4st4rCr4ck">M4st4rCr4ck</a> </td>
                <td> C/C++ </td>
                <td> x86 </td>
                <td> 1.4 </td>
                <td> 3.4 </td>
                <td> Unix/linux etc. </td>
                <td> 5:12 PM 01/12/2024 </td>
                <td> 1 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/659fde9deef082e477ff59ba">nice_crackme</a></td>
                <td> <a href="/user/Jenya">Jenya</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.3 </td>
                <td> 3.8 </td>
                <td> Unix/linux etc. </td>
                <td> 12:27 PM 01/11/2024 </td>
                <td> 1 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/65727e2035240bf986f0ff19">Weird</a></td>
                <td> <a href="/user/exzettabyte">exzettabyte</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.2 </td>
                <td> Unix/linux etc. </td>
                <td> 2:23 AM 12/08/2023 </td>
                <td> 1 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/655b43750f4238b24302bc42">linux_asm_jenya</a></td>
                <td> <a href="/user/Jenya">Jenya</a> </td>
                <td> Assembler </td>
                <td> x86-64 </td>
                <td> 1.5 </td>
                <td> 5.2 </td>
                <td> Unix/linux etc. </td>
                <td> 11:31 AM 11/20/2023 </td>
                <td> 0 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/6513567328b5870bef263329">Plain sight</a></td>
                <td> <a href="/user/I3a4dam">I3a4dam</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.0 </td>
                <td> 3.7 </td>
                <td> Unix/linux etc. </td>
                <td> 10:08 PM 09/26/2023 </td>
                <td> 5 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/64fdf93bd931496abf90994b">based</a></td>
                <td> <a href="/user/mt77">mt77</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.3 </td>
                <td> 4.1 </td>
                <td> Unix/linux etc. </td>
                <td> 5:13 PM 09/10/2023 </td>
                <td> 5 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/64e91b92d931496abf9091e3">Find password</a></td>
                <td> <a href="/user/ithawk">ithawk</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.9 </td>
                <td> 3.8 </td>
                <td> Unix/linux etc. </td>
                <td> 9:22 PM 08/25/2023 </td>
                <td> 4 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/646627a933c5d439389131d9"> Level1</a></td>
                <td> <a href="/user/sudo0x18">sudo0x18</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.1 </td>
                <td> 4.2 </td>
                <td> Unix/linux etc. </td>
                <td> 1:27 PM 05/18/2023 </td>
                <td> 15 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/645d3d4e33c5d43938913079">GDB basics</a></td>
                <td> <a href="/user/Varsovie">Varsovie</a> </td>
                <td> C/C++ </td>
                <td> x86 </td>
                <td> 1.5 </td>
                <td> 4.9 </td>
                <td> Unix/linux etc. </td>
                <td> 7:09 PM 05/11/2023 </td>
                <td> 4 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/6454d06c33c5d43938912e8a">Vending Machine</a></td>
                <td> <a href="/user/Yekong">Yekong</a> </td>
                <td> Unspecified/other </td>
                <td> x86-64 </td>
                <td> 1.6 </td>
                <td> 5.2 </td>
                <td> Unix/linux etc. </td>
                <td> 9:46 AM 05/05/2023 </td>
                <td> 1 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/644bd78b33c5d43938912c94">Salt and Hash - Linux</a></td>
                <td> <a href="/user/Yekong">Yekong</a> </td>
                <td> Unspecified/other </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 2:26 PM 04/28/2023 </td>
                <td> 0 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/644af68433c5d43938912c6b">My first crackme</a></td>
                <td> <a href="/user/ss1ned">ss1ned</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.4 </td>
                <td> 4.3 </td>
                <td> Unix/linux etc. </td>
                <td> 10:26 PM 04/27/2023 </td>
                <td> 1 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/641cc0a133c5d447bc761be0">Beginner Friendly</a></td>
                <td> <a href="/user/basyl">basyl</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.0 </td>
                <td> 2.9 </td>
                <td> Unix/linux etc. </td>
                <td> 9:12 PM 03/23/2023 </td>
                <td> 1 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/6419d74e33c5d447bc761afa">baby</a></td>
                <td> <a href="/user/ghost256">ghost256</a> </td>
                <td> C/C++ </td>
                <td> other </td>
                <td> 2.0 </td>
                <td> 3.8 </td>
                <td> Unix/linux etc. </td>
                <td> 4:11 PM 03/21/2023 </td>
                <td> 0 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/63c4ee1a33c5d43ab4ecf49a">Just In Time</a></td>
                <td> <a href="/user/skibur">skibur</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.2 </td>
                <td> Unix/linux etc. </td>
                <td> 6:26 AM 01/16/2023 </td>
                <td> 3 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/637c66b633c5d43ab4ecec2a">Illogical Logic</a></td>
                <td> <a href="/user/marufmurtuza">marufmurtuza</a> </td>
                <td> C/C++ </td>
                <td> x86 </td>
                <td> 1.4 </td>
                <td> 2.8 </td>
                <td> Unix/linux etc. </td>
                <td> 6:05 AM 11/22/2022 </td>
                <td> 3 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/632cf67b33c5d4425e2cd501">FindThePassword1</a></td>
                <td> <a href="/user/Xeeven">Xeeven</a> </td>
                <td> Assembler </td>
                <td> x86 </td>
                <td> 1.0 </td>
                <td> 4.2 </td>
                <td> Unix/linux etc. </td>
                <td> 11:57 PM 09/22/2022 </td>
                <td> 5 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/629e1e5833c5d4251e72375f">find a real key</a></td>
                <td> <a href="/user/f0rizen">f0rizen</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.7 </td>
                <td> Unix/linux etc. </td>
                <td> 3:33 PM 06/06/2022 </td>
                <td> 7 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/6296c1ff33c5d45b75903c0f">my_f1rs7_cr4ckm3</a></td>
                <td> <a href="/user/b3nd3p">b3nd3p</a> </td>
                <td> C/C++ </td>
                <td> x86 </td>
                <td> 1.2 </td>
                <td> 3.6 </td>
                <td> Unix/linux etc. </td>
                <td> 1:33 AM 06/01/2022 </td>
                <td> 1 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/62327b0433c5d46c8bcc0335">licesnse_checker_3</a></td>
                <td> <a href="/user/pourmeadrinkwhileimfloating">pourmeadrinkwhileimfloating</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.5 </td>
                <td> 3.4 </td>
                <td> Unix/linux etc. </td>
                <td> 12:04 AM 03/17/2022 </td>
                <td> 2 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/62072dd633c5d46c8bcbfd9b">License Checker 0x03</a></td>
                <td> <a href="/user/NomanProdhan">NomanProdhan</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.8 </td>
                <td> 4.1 </td>
                <td> Unix/linux etc. </td>
                <td> 3:47 AM 02/12/2022 </td>
                <td> 6 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/61efb6a633c5d413767ca678">Eat Sleep Trace Repeat</a></td>
                <td> <a href="/user/X3eRo0">X3eRo0</a> </td>
                <td> Assembler </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.5 </td>
                <td> Unix/linux etc. </td>
                <td> 8:36 AM 01/25/2022 </td>
                <td> 1 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/61e9983133c5d413767ca5ac">gugus the first</a></td>
                <td> <a href="/user/bueb810">bueb810</a> </td>
                <td> C/C++ </td>
                <td> x86 </td>
                <td> 1.8 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 5:13 PM 01/20/2022 </td>
                <td> 4 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/61c8deff33c5d413767ca0ea">TryCrackMe</a></td>
                <td> <a href="/user/MrEmpy">MrEmpy</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.7 </td>
                <td> 4.2 </td>
                <td> Unix/linux etc. </td>
                <td> 9:30 PM 12/26/2021 </td>
                <td> 1 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/61c8b23a33c5d413767ca0de">x64_crackme_keygen</a></td>
                <td> <a href="/user/dev0">dev0</a> </td>
                <td> Assembler </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 3.4 </td>
                <td> Unix/linux etc. </td>
                <td> 6:19 PM 12/26/2021 </td>
                <td> 2 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/61c62bde33c5d413767ca0a0">License Checker 0x02</a></td>
                <td> <a href="/user/NomanProdhan">NomanProdhan</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.1 </td>
                <td> 3.9 </td>
                <td> Unix/linux etc. </td>
                <td> 8:21 PM 12/24/2021 </td>
                <td> 3 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/619eda7b33c5d455dece628d">License Checker 0x01</a></td>
                <td> <a href="/user/NomanProdhan">NomanProdhan</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.1 </td>
                <td> 3.8 </td>
                <td> Unix/linux etc. </td>
                <td> 12:36 AM 11/25/2021 </td>
                <td> 1 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/612e85d833c5d41acedffa4f">PleaseCrackMe</a></td>
                <td> <a href="/user/RaphDev">RaphDev</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.4 </td>
                <td> 4.4 </td>
                <td> Unix/linux etc. </td>
                <td> 7:41 PM 08/31/2021 </td>
                <td> 12 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/611e9bfb33c5d45db85dc2d7">super_easy</a></td>
                <td> <a href="/user/eventhorizon02">eventhorizon02</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.8 </td>
                <td> 4.8 </td>
                <td> Unix/linux etc. </td>
                <td> 5:59 PM 08/19/2021 </td>
                <td> 7 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/611e76ec33c5d45db85dc2d1">4N0NY31TY's First Crackme</a></td>
                <td> <a href="/user/4N0NY31TY">4N0NY31TY</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.5 </td>
                <td> 4.4 </td>
                <td> Unix/linux etc. </td>
                <td> 3:21 PM 08/19/2021 </td>
                <td> 4 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/60fc687b33c5d42814fb34e0">revv</a></td>
                <td> <a href="/user/0xtamsee1">0xtamsee1</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.8 </td>
                <td> 4.4 </td>
                <td> Unix/linux etc. </td>
                <td> 7:22 PM 07/24/2021 </td>
                <td> 11 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/60f31f1d33c5d42814fb3381">Forest</a></td>
                <td> <a href="/user/MKesenheimer">MKesenheimer</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.7 </td>
                <td> 4.3 </td>
                <td> Unix/linux etc. </td>
                <td> 6:19 PM 07/17/2021 </td>
                <td> 4 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/60d766c033c5d410b8843039">My First Crackme</a></td>
                <td> <a href="/user/mahjestic">mahjestic</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.1 </td>
                <td> 2.6 </td>
                <td> Unix/linux etc. </td>
                <td> 5:41 PM 06/26/2021 </td>
                <td> 1 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/60bd61ea33c5d410b8842c76">Yariza Crackme #2</a></td>
                <td> <a href="/user/yariza">yariza</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.7 </td>
                <td> 3.8 </td>
                <td> Unix/linux etc. </td>
                <td> 12:01 AM 06/07/2021 </td>
                <td> 1 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/60957b9a33c5d458ce0ec88e">EZwan</a></td>
                <td> <a href="/user/DirkD">DirkD</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.8 </td>
                <td> 4.2 </td>
                <td> Unix/linux etc. </td>
                <td> 5:40 PM 05/07/2021 </td>
                <td> 3 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/6074618733c5d44899821e35">My_first_ever_crackme</a></td>
                <td> <a href="/user/ASBO_GENERAL">ASBO_GENERAL</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.9 </td>
                <td> 3.6 </td>
                <td> Unix/linux etc. </td>
                <td> 3:04 PM 04/12/2021 </td>
                <td> 6 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/6047ffb433c5d42c3d016da6">crackme</a></td>
                <td> <a href="/user/Harel21">Harel21</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.6 </td>
                <td> 4.5 </td>
                <td> Unix/linux etc. </td>
                <td> 11:07 PM 03/09/2021 </td>
                <td> 8 </td>
                <td> 1 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/6044083333c5d42c3d016d3d">GO GO GO - Harmful Logic</a></td>
                <td> <a href="/user/s0k1t">s0k1t</a> </td>
                <td> Unspecified/other </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:54 PM 03/06/2021 </td>
                <td> 1 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5fda4fa433c5d41f64dee37b">lockcode</a></td>
                <td> <a href="/user/SilentWraith">SilentWraith</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.8 </td>
                <td> 3.5 </td>
                <td> Unix/linux etc. </td>
                <td> 6:19 PM 12/16/2020 </td>
                <td> 6 </td>
                <td> 5 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5fd5c44c33c5d424269a1b76">what</a></td>
                <td> <a href="/user/rafi">rafi</a> </td>
                <td> Unspecified/other </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 7:35 AM 12/13/2020 </td>
                <td> 2 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5fcfb87933c5d424269a1afc">EZ crackme</a></td>
                <td> <a href="/user/R3tr0BS">R3tr0BS</a> </td>
                <td> Assembler </td>
                <td> x86 </td>
                <td> 1.0 </td>
                <td> 3.8 </td>
                <td> Unix/linux etc. </td>
                <td> 5:31 PM 12/08/2020 </td>
                <td> 12 </td>
                <td> 3 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5fa94bb233c5d424269a17b7">Personal Safe</a></td>
                <td> <a href="/user/LubimPiskoty">LubimPiskoty</a> </td>
                <td> Assembler </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 5.0 </td>
                <td> Unix/linux etc. </td>
                <td> 2:01 PM 11/09/2020 </td>
                <td> 2 </td>
                <td> 6 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5fa2cdce33c5d424269a1740">Just crackme</a></td>
                <td> <a href="/user/tynkute">tynkute</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 2.5 </td>
                <td> Unix/linux etc. </td>
                <td> 3:50 PM 11/04/2020 </td>
                <td> 1 </td>
                <td> 5 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5f4efbb133c5d4357b3b00a0">Date of Birth</a></td>
                <td> <a href="/user/jeffli6789">jeffli6789</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 1:56 AM 09/02/2020 </td>
                <td> 1 </td>
                <td> 7 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5f3d7ed033c5d42a7c667d95">rop</a></td>
                <td> <a href="/user/BitFriends">BitFriends</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 5.0 </td>
                <td> Unix/linux etc. </td>
                <td> 7:34 PM 08/19/2020 </td>
                <td> 1 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5f0998cb33c5d42a7c667974">Crack_5</a></td>
                <td> <a href="/user/D4RKFL0W">D4RKFL0W</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:47 AM 07/11/2020 </td>
                <td> 1 </td>
                <td> 2 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5f05ec3c33c5d42a7c66792b">simple overflow</a></td>
                <td> <a href="/user/BitFriends">BitFriends</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.4 </td>
                <td> 5.0 </td>
                <td> Unix/linux etc. </td>
                <td> 3:54 PM 07/08/2020 </td>
                <td> 11 </td>
                <td> 5 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5f01df5633c5d4285070948b">x86</a></td>
                <td> <a href="/user/jeffli6789">jeffli6789</a> </td>
                <td> Assembler </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 2:10 PM 07/05/2020 </td>
                <td> 1 </td>
                <td> 2 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5f00a02533c5d4285070947a">bubbly</a></td>
                <td> <a href="/user/jeffli6789">jeffli6789</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.5 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 3:28 PM 07/04/2020 </td>
                <td> 2 </td>
                <td> 8 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5eea811d33c5d449d91ae870">ShAPK1</a></td>
                <td> <a href="/user/destructeur">destructeur</a> </td>
                <td> Java </td>
                <td> other </td>
                <td> 2.0 </td>
                <td> 4.2 </td>
                <td> Unix/linux etc. </td>
                <td> 8:46 PM 06/17/2020 </td>
                <td> 4 </td>
                <td> 5 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ed0584b33c5d449d91ae67b">Guess_my_name</a></td>
                <td> <a href="/user/mrmtg">mrmtg</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.1 </td>
                <td> 3.3 </td>
                <td> Unix/linux etc. </td>
                <td> 12:33 AM 05/29/2020 </td>
                <td> 2 </td>
                <td> 7 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ecd7cc133c5d449d91ae641">ZED-Crackme</a></td>
                <td> <a href="/user/zed-zahir">zed-zahir</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 8:32 PM 05/26/2020 </td>
                <td> 6 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ecb906533c5d449d91ae616">timotei crackme#4</a></td>
                <td> <a href="/user/tim0tei">tim0tei</a> </td>
                <td> Assembler </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.5 </td>
                <td> Unix/linux etc. </td>
                <td> 9:31 AM 05/25/2020 </td>
                <td> 1 </td>
                <td> 2 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ecb902633c5d449d91ae615">timotei crackme#3</a></td>
                <td> <a href="/user/tim0tei">tim0tei</a> </td>
                <td> Assembler </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.5 </td>
                <td> Unix/linux etc. </td>
                <td> 9:30 AM 05/25/2020 </td>
                <td> 1 </td>
                <td> 3 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ec1a37533c5d449d91ae535">Baby Ransom</a></td>
                <td> <a href="/user/Shad3">Shad3</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.3 </td>
                <td> 4.8 </td>
                <td> Unix/linux etc. </td>
                <td> 8:49 PM 05/17/2020 </td>
                <td> 2 </td>
                <td> 7 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5eae2d6633c5d47611746500">easyAF</a></td>
                <td> <a href="/user/476f64">476f64</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.0 </td>
                <td> 3.6 </td>
                <td> Unix/linux etc. </td>
                <td> 2:33 AM 05/03/2020 </td>
                <td> 17 </td>
                <td> 11 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ea48a1433c5d47611746436">nasm crack</a></td>
                <td> <a href="/user/BitFriends">BitFriends</a> </td>
                <td> Assembler </td>
                <td> x86-64 </td>
                <td> 1.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 7:05 PM 04/25/2020 </td>
                <td> 13 </td>
                <td> 5 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5e83f7f433c5d4439bb2e059">Small Keygenme</a></td>
                <td> <a href="/user/BinaryNewbie">BinaryNewbie</a> </td>
                <td> Assembler </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 2:09 AM 04/01/2020 </td>
                <td> 2 </td>
                <td> 10 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5e7a61ca33c5d4439bb2df60">timotei crackme#2 	</a></td>
                <td> <a href="/user/tim0tei">tim0tei</a> </td>
                <td> Assembler </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.5 </td>
                <td> Unix/linux etc. </td>
                <td> 7:38 PM 03/24/2020 </td>
                <td> 1 </td>
                <td> 1 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5e76c37d33c5d4439bb2df1b">racecars</a></td>
                <td> <a href="/user/chillywilly">chillywilly</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 1:46 AM 03/22/2020 </td>
                <td> 1 </td>
                <td> 7 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5e74a49833c5d4439bb2def5">admin_panel</a></td>
                <td> <a href="/user/BitFriends">BitFriends</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 11:10 AM 03/20/2020 </td>
                <td> 1 </td>
                <td> 17 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5e6ac90233c5d4439bb2de39">Very Special Number v1</a></td>
                <td> <a href="/user/owo_whats_this">owo_whats_this</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 11:42 PM 03/12/2020 </td>
                <td> 2 </td>
                <td> 2 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5e604d4333c5d4439bb2dd72">mgdilolmsoamasiug</a></td>
                <td> <a href="/user/raphiolet">raphiolet</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 12:52 AM 03/05/2020 </td>
                <td> 5 </td>
                <td> 2 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5e5c14c333c5d4439bb2dd1f">timotei crackme#1</a></td>
                <td> <a href="/user/timotei">timotei</a> </td>
                <td> Assembler </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.5 </td>
                <td> Unix/linux etc. </td>
                <td> 8:02 PM 03/01/2020 </td>
                <td> 1 </td>
                <td> 6 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5e567e1d33c5d4439bb2dca0">Lucky Numbers</a></td>
                <td> <a href="/user/oguzbey">oguzbey</a> </td>
                <td> Assembler </td>
                <td> x86 </td>
                <td> 1.3 </td>
                <td> 5.0 </td>
                <td> Unix/linux etc. </td>
                <td> 2:18 PM 02/26/2020 </td>
                <td> 7 </td>
                <td> 8 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5e0fa43b33c5d419aa01351e">Crackme-4</a></td>
                <td> <a href="/user/D4RKFL0W">D4RKFL0W</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.7 </td>
                <td> 4.7 </td>
                <td> Unix/linux etc. </td>
                <td> 8:29 PM 01/03/2020 </td>
                <td> 4 </td>
                <td> 5 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5dfd77a833c5d419aa013406">Ext.challenges</a></td>
                <td> <a href="/user/Exxtra12">Exxtra12</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 1:38 AM 12/21/2019 </td>
                <td> 1 </td>
                <td> 8 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5df26b4033c5d419aa013362">glow wine [keygen practice]</a></td>
                <td> <a href="/user/Bkamp">Bkamp</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.6 </td>
                <td> 4.5 </td>
                <td> Unix/linux etc. </td>
                <td> 4:30 PM 12/12/2019 </td>
                <td> 8 </td>
                <td> 8 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5dce805c33c5d419aa0131ae">half-twins</a></td>
                <td> <a href="/user/m3hd1">m3hd1</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:39 AM 11/15/2019 </td>
                <td> 5 </td>
                <td> 5 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5da31ebc33c5d46f00e2c661">easy keyg3nme</a></td>
                <td> <a href="/user/ezman">ezman</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.4 </td>
                <td> 4.9 </td>
                <td> Unix/linux etc. </td>
                <td> 12:55 PM 10/13/2019 </td>
                <td> 4 </td>
                <td> 27 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5d78168833c5d46f00e2c428">alien_bin</a></td>
                <td> <a href="/user/totothetoro">totothetoro</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 9:32 PM 09/10/2019 </td>
                <td> 2 </td>
                <td> 7 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5d6da7bc33c5d46f00e2c3a3">Simple obfuscation</a></td>
                <td> <a href="/user/BinaryNewbie">BinaryNewbie</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 11:37 PM 09/02/2019 </td>
                <td> 2 </td>
                <td> 13 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5d64749533c5d46f00e2c324">Election</a></td>
                <td> <a href="/user/paypain">paypain</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 12:08 AM 08/27/2019 </td>
                <td> 1 </td>
                <td> 3 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5d46d2bd33c5d444ad3018d3">Crack the algorithm</a></td>
                <td> <a href="/user/skudo">skudo</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.5 </td>
                <td> Unix/linux etc. </td>
                <td> 12:42 PM 08/04/2019 </td>
                <td> 2 </td>
                <td> 2 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5d41bf7633c5d444ad30189b">Save Scooby</a></td>
                <td> <a href="/user/mrT4ntr4">mrT4ntr4</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.7 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 4:19 PM 07/31/2019 </td>
                <td> 5 </td>
                <td> 21 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5d24585133c5d410dc4d0cbd">keygenme</a></td>
                <td> <a href="/user/kawaii-flesh">kawaii-flesh</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.7 </td>
                <td> Unix/linux etc. </td>
                <td> 9:03 AM 07/09/2019 </td>
                <td> 2 </td>
                <td> 6 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5d1a344033c5d410dc4d0c3e">guild hall adventure Ch.2</a></td>
                <td> <a href="/user/ker2x">ker2x</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.5 </td>
                <td> Unix/linux etc. </td>
                <td> 4:26 PM 07/01/2019 </td>
                <td> 5 </td>
                <td> 9 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5d17962b33c5d41c6d56e1f2">Key and keygen</a></td>
                <td> <a href="/user/kawaii-flesh">kawaii-flesh</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 4:47 PM 06/29/2019 </td>
                <td> 1 </td>
                <td> 2 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5d0fa1ac33c5d41c6d56e172">guild hall adventure Ch.1</a></td>
                <td> <a href="/user/ker2x">ker2x</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.2 </td>
                <td> 4.4 </td>
                <td> Unix/linux etc. </td>
                <td> 3:58 PM 06/23/2019 </td>
                <td> 11 </td>
                <td> 17 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5d0d1e1333c5d41c6d56e155">Simple crackme</a></td>
                <td> <a href="/user/kawaii-flesh">kawaii-flesh</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 6:12 PM 06/21/2019 </td>
                <td> 5 </td>
                <td> 2 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5d09368533c5d41c6d56e124">Time is of the Essence</a></td>
                <td> <a href="/user/emiflake">emiflake</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 2.7 </td>
                <td> Unix/linux etc. </td>
                <td> 7:07 PM 06/18/2019 </td>
                <td> 2 </td>
                <td> 3 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5d07f03233c5d41c6d56e10c">Quick Crypto, 18k</a></td>
                <td> <a href="/user/andrewl">andrewl</a> </td>
                <td> Assembler </td>
                <td> x86 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 7:55 PM 06/17/2019 </td>
                <td> 1 </td>
                <td> 3 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5cf574fe33c5d41c6d56e01b">crackme #1</a></td>
                <td> <a href="/user/hikilaka">hikilaka</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 7:29 PM 06/03/2019 </td>
                <td> 0 </td>
                <td> 1 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ce137b933c5d4419da55ac2">D4RK_FL0W-3.5</a></td>
                <td> <a href="/user/D4RKFL0W">D4RKFL0W</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 11:02 AM 05/19/2019 </td>
                <td> 3 </td>
                <td> 5 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ccf3bf333c5d4419da559bd">Sh4ll10</a></td>
                <td> <a href="/user/destructeur">destructeur</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.5 </td>
                <td> 4.5 </td>
                <td> Unix/linux etc. </td>
                <td> 7:39 PM 05/05/2019 </td>
                <td> 10 </td>
                <td> 18 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ccecc7e33c5d4419da559b3">crackmepal</a></td>
                <td> <a href="/user/novn91">novn91</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.5 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 11:43 AM 05/05/2019 </td>
                <td> 6 </td>
                <td> 8 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5cc1117833c5d4419da558dc">EasyCrack - Much0l0k0</a></td>
                <td> <a href="/user/paypain">paypain</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.5 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 1:46 AM 04/25/2019 </td>
                <td> 7 </td>
                <td> 9 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5cb7533133c5d4419da5584b">am i really random?</a></td>
                <td> <a href="/user/m00ny">m00ny</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 4:24 PM 04/17/2019 </td>
                <td> 1 </td>
                <td> 3 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ca0b6c833c5d4419da5567b">Password Login 2</a></td>
                <td> <a href="/user/Loz">Loz</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 12:47 PM 03/31/2019 </td>
                <td> 2 </td>
                <td> 4 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ca0b3f833c5d4419da5567a">Crack3-by-D4RK_FL0W</a></td>
                <td> <a href="/user/D4RKFL0W">D4RKFL0W</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 12:35 PM 03/31/2019 </td>
                <td> 2 </td>
                <td> 5 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5c9d9eea33c5d4419da55641">de_tcrack1</a></td>
                <td> <a href="/user/paypain">paypain</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 4:28 AM 03/29/2019 </td>
                <td> 0 </td>
                <td> 2 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5c90a72d33c5d4776a837f07">Password Login</a></td>
                <td> <a href="/user/Loz">Loz</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 8:24 AM 03/19/2019 </td>
                <td> 7 </td>
                <td> 9 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5c8e1a9533c5d4776a837ecf">Easy_firstCrackme-by-D4RK_FL0W</a></td>
                <td> <a href="/user/D4RKFL0W">D4RKFL0W</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.5 </td>
                <td> 4.5 </td>
                <td> Unix/linux etc. </td>
                <td> 9:59 AM 03/17/2019 </td>
                <td> 5 </td>
                <td> 8 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5c8d45c333c5d4776a837ec2">Keygen Practice</a></td>
                <td> <a href="/user/inxaneninja">inxaneninja</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.3 </td>
                <td> Unix/linux etc. </td>
                <td> 6:51 PM 03/16/2019 </td>
                <td> 5 </td>
                <td> 3 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5c53840a33c5d475210bc6e9">crackme-not</a></td>
                <td> <a href="/user/weissi1994">weissi1994</a> </td>
                <td> Assembler </td>
                <td> x86-64 </td>
                <td> 1.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 11:26 PM 01/31/2019 </td>
                <td> 7 </td>
                <td> 9 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5c2acb8933c5d46a3882b8d4">Simple Keygen</a></td>
                <td> <a href="/user/Yuri">Yuri</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.5 </td>
                <td> 5.0 </td>
                <td> Unix/linux etc. </td>
                <td> 2:08 AM 01/01/2019 </td>
                <td> 8 </td>
                <td> 20 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5c268e8333c5d41e58e00654">keyGme</a></td>
                <td> <a href="/user/rion">rion</a> </td>
                <td> C/C++ </td>
                <td> x86 </td>
                <td> 2.0 </td>
                <td> 4.7 </td>
                <td> Unix/linux etc. </td>
                <td> 8:58 PM 12/28/2018 </td>
                <td> 2 </td>
                <td> 7 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5c2335c033c5d41e58e00625">c1_keygenme1</a></td>
                <td> <a href="/user/c1">c1</a> </td>
                <td> C/C++ </td>
                <td> x86 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 8:03 AM 12/26/2018 </td>
                <td> 1 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5c1cc7d533c5d41e58e005ee">easy_keygenme </a></td>
                <td> <a href="/user/bahha">bahha</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 11:00 AM 12/21/2018 </td>
                <td> 2 </td>
                <td> 1 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5c11e2f333c5d41e58e0057a">WhiteRabbit</a></td>
                <td> <a href="/user/nutcake">nutcake</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.3 </td>
                <td> 2.5 </td>
                <td> Unix/linux etc. </td>
                <td> 4:41 AM 12/13/2018 </td>
                <td> 7 </td>
                <td> 4 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5c11e1f333c5d41e58e00579">PieIsMyFav</a></td>
                <td> <a href="/user/nutcake">nutcake</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 4:37 AM 12/13/2018 </td>
                <td> 8 </td>
                <td> 6 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5c11dcaf33c5d41e58e00578">PrettyDamnEasy</a></td>
                <td> <a href="/user/nutcake">nutcake</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.0 </td>
                <td> 3.6 </td>
                <td> Unix/linux etc. </td>
                <td> 4:14 AM 12/13/2018 </td>
                <td> 6 </td>
                <td> 11 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5bc98bcc33c5d4110a29b2cc">undebuggable</a></td>
                <td> <a href="/user/daniellimws">daniellimws</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 7:46 AM 10/19/2018 </td>
                <td> 1 </td>
                <td> 5 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5b9d312233c5d45fc286ae03">noprelo</a></td>
                <td> <a href="/user/kellek">kellek</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 4:19 PM 09/15/2018 </td>
                <td> 1 </td>
                <td> 10 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5b9a0b2433c5d45fc286adec">prodigy</a></td>
                <td> <a href="/user/fack">fack</a> </td>
                <td> C/C++ </td>
                <td> x86 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 7:00 AM 09/13/2018 </td>
                <td> 1 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5b8a37a433c5d45fc286ad83">easy_reverse</a></td>
                <td> <a href="/user/cbm-hackers">cbm-hackers</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.3 </td>
                <td> 4.8 </td>
                <td> Unix/linux etc. </td>
                <td> 6:54 AM 09/01/2018 </td>
                <td> 32 </td>
                <td> 43 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5b8101c833c5d41f5c6ba945">CedeCe 16</a></td>
                <td> <a href="/user/exzettabyte">exzettabyte</a> </td>
                <td> C/C++ </td>
                <td> x86 </td>
                <td> 1.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 7:14 AM 08/25/2018 </td>
                <td> 6 </td>
                <td> 1 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5b81014933c5d41f5c6ba944">JustSee</a></td>
                <td> <a href="/user/exzettabyte">exzettabyte</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.2 </td>
                <td> 4.2 </td>
                <td> Unix/linux etc. </td>
                <td> 7:12 AM 08/25/2018 </td>
                <td> 11 </td>
                <td> 8 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5b5b386033c5d46b771434b8">Crack The Door</a></td>
                <td> <a href="/user/S01den">S01den</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 3:21 PM 07/27/2018 </td>
                <td> 3 </td>
                <td> 5 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5b1403c633c5d41557b02273">Sh4ll5</a></td>
                <td> <a href="/user/destructeur">destructeur</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 3:05 PM 06/03/2018 </td>
                <td> 2 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5b0b181a33c5d406c0abcd09">Sh4ll4</a></td>
                <td> <a href="/user/destructeur">destructeur</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 8:42 PM 05/27/2018 </td>
                <td> 4 </td>
                <td> 3 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5aef385633c5d41ac64b492f">Sh4ll2</a></td>
                <td> <a href="/user/destructeur">destructeur</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 5:16 PM 05/06/2018 </td>
                <td> 4 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5aef37c733c5d41ac64b492e">Sh4ll1</a></td>
                <td> <a href="/user/destructeur">destructeur</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 5:13 PM 05/06/2018 </td>
                <td> 21 </td>
                <td> 10 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ab77f6633c5d40ad448cbfe">mycrk by cli3nt</a></td>
                <td> <a href="/user/crackmes.de">crackmes.de</a> </td>
                <td> C/C++ </td>
                <td> x86 </td>
                <td> 1.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:52 AM 03/25/2018 </td>
                <td> 6 </td>
                <td> 1 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ab77f6533c5d40ad448cbc1">crackme.01.32 by geyslan</a></td>
                <td> <a href="/user/crackmes.de">crackmes.de</a> </td>
                <td> C/C++ </td>
                <td> x86 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:52 AM 03/25/2018 </td>
                <td> 4 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ab77f6533c5d40ad448cb97">kgm1 by ascii</a></td>
                <td> <a href="/user/crackmes.de">crackmes.de</a> </td>
                <td> C/C++ </td>
                <td> x86 </td>
                <td> 1.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:52 AM 03/25/2018 </td>
                <td> 6 </td>
                <td> 1 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ab77f6533c5d40ad448cb74">f1nd_my_k3y5 by rezk2ll</a></td>
                <td> <a href="/user/crackmes.de">crackmes.de</a> </td>
                <td> Assembler </td>
                <td> x86 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:52 AM 03/25/2018 </td>
                <td> 1 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ab77f6533c5d40ad448cb73">keygenmenasm by rezk2ll</a></td>
                <td> <a href="/user/crackmes.de">crackmes.de</a> </td>
                <td> Assembler </td>
                <td> x86 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:52 AM 03/25/2018 </td>
                <td> 5 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ab77f6533c5d40ad448cb72">beatme by rezk2ll</a></td>
                <td> <a href="/user/crackmes.de">crackmes.de</a> </td>
                <td> Assembler </td>
                <td> x86 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:52 AM 03/25/2018 </td>
                <td> 3 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ab77f6533c5d40ad448cb71">crackme_nasm by rezk2ll</a></td>
                <td> <a href="/user/crackmes.de">crackmes.de</a> </td>
                <td> Assembler </td>
                <td> x86 </td>
                <td> 1.3 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:52 AM 03/25/2018 </td>
                <td> 10 </td>
                <td> 4 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ab77f6533c5d40ad448cb67">my_first_crackme by bertels</a></td>
                <td> <a href="/user/crackmes.de">crackmes.de</a> </td>
                <td> Unspecified/other </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:52 AM 03/25/2018 </td>
                <td> 1 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ab77f6433c5d40ad448caf9">keygenme228 by profdraculare</a></td>
                <td> <a href="/user/crackmes.de">crackmes.de</a> </td>
                <td> C/C++ </td>
                <td> x86 </td>
                <td> 1.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:52 AM 03/25/2018 </td>
                <td> 2 </td>
                <td> 1 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ab77f6433c5d40ad448cae0">my_first_crack_me by oddcoder</a></td>
                <td> <a href="/user/crackmes.de">crackmes.de</a> </td>
                <td> C/C++ </td>
                <td> x86 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:52 AM 03/25/2018 </td>
                <td> 3 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ab77f6333c5d40ad448ca8b">easy_crackme_2 by lord</a></td>
                <td> <a href="/user/crackmes.de">crackmes.de</a> </td>
                <td> Assembler </td>
                <td> x86 </td>
                <td> 1.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:52 AM 03/25/2018 </td>
                <td> 7 </td>
                <td> 1 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ab77f6333c5d40ad448ca8a">easy_linux_crackme by lord</a></td>
                <td> <a href="/user/crackmes.de">crackmes.de</a> </td>
                <td> Assembler </td>
                <td> x86 </td>
                <td> 1.0 </td>
                <td> 2.5 </td>
                <td> Unix/linux etc. </td>
                <td> 10:52 AM 03/25/2018 </td>
                <td> 6 </td>
                <td> 1 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ab77f6333c5d40ad448ca50">crackmypadre by mazrock</a></td>
                <td> <a href="/user/crackmes.de">crackmes.de</a> </td>
                <td> C/C++ </td>
                <td> x86 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:52 AM 03/25/2018 </td>
                <td> 6 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ab77f6333c5d40ad448ca01">lincrackme1 by adrianbn</a></td>
                <td> <a href="/user/crackmes.de">crackmes.de</a> </td>
                <td> C/C++ </td>
                <td> x86 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:52 AM 03/25/2018 </td>
                <td> 4 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ab77f6233c5d40ad448c9fa">keygenme_1 by mre521</a></td>
                <td> <a href="/user/crackmes.de">crackmes.de</a> </td>
                <td> C/C++ </td>
                <td> x86 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:52 AM 03/25/2018 </td>
                <td> 3 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ab77f6233c5d40ad448c9eb">easy_math by intsig</a></td>
                <td> <a href="/user/crackmes.de">crackmes.de</a> </td>
                <td> C/C++ </td>
                <td> x86 </td>
                <td> 1.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:52 AM 03/25/2018 </td>
                <td> 4 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ab77f6233c5d40ad448c9ea">64bit_confusion by intsig</a></td>
                <td> <a href="/user/crackmes.de">crackmes.de</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:52 AM 03/25/2018 </td>
                <td> 1 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ab77f6233c5d40ad448c9e3">vvsc by elijunior01</a></td>
                <td> <a href="/user/crackmes.de">crackmes.de</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:52 AM 03/25/2018 </td>
                <td> 4 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ab77f6233c5d40ad448c9c3">yyyyyyy1 by yyyyyyy</a></td>
                <td> <a href="/user/crackmes.de">crackmes.de</a> </td>
                <td> Assembler </td>
                <td> x86 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:52 AM 03/25/2018 </td>
                <td> 1 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ab77f6133c5d40ad448c940">simplepin by thetrh51</a></td>
                <td> <a href="/user/crackmes.de">crackmes.de</a> </td>
                <td> C/C++ </td>
                <td> x86 </td>
                <td> 1.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:52 AM 03/25/2018 </td>
                <td> 4 </td>
                <td> 1 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ab77f6033c5d40ad448c8c4">crackme_de2_1 by rgcalsaverini</a></td>
                <td> <a href="/user/crackmes.de">crackmes.de</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 1.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:52 AM 03/25/2018 </td>
                <td> 1 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ab77f6033c5d40ad448c8b7">berkeley by kwisatz_haderach</a></td>
                <td> <a href="/user/crackmes.de">crackmes.de</a> </td>
                <td> C/C++ </td>
                <td> x86 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:52 AM 03/25/2018 </td>
                <td> 2 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ab77f6033c5d40ad448c8b0">rascal999s_crackme_serial_challenge by rascal999</a></td>
                <td> <a href="/user/crackmes.de">crackmes.de</a> </td>
                <td> Unspecified/other </td>
                <td> x86 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:52 AM 03/25/2018 </td>
                <td> 1 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ab77f5f33c5d40ad448c800">code_linux by buga0205</a></td>
                <td> <a href="/user/crackmes.de">crackmes.de</a> </td>
                <td> C/C++ </td>
                <td> x86 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:52 AM 03/25/2018 </td>
                <td> 1 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ab77f5f33c5d40ad448c7bd">basic_logic by eholzbach</a></td>
                <td> <a href="/user/crackmes.de">crackmes.de</a> </td>
                <td> Assembler </td>
                <td> x86 </td>
                <td> 1.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:52 AM 03/25/2018 </td>
                <td> 4 </td>
                <td> 0 </td>
            </tr>
            
            <tr class="text-center">
                <td> <a href="/crackme/5ab77f5e33c5d40ad448c78d">crackme2 by seveb</a></td>
                <td> <a href="/user/crackmes.de">crackmes.de</a> </td>
                <td> C/C++ </td>
                <td> x86-64 </td>
                <td> 2.0 </td>
                <td> 4.0 </td>
                <td> Unix/linux etc. </td>
                <td> 10:52 AM 03/25/2018 </td>
                <td> 4 </td>
                <td> 0 </td>
            </tr>
            
        </tbody>
    </table>
</div>

<footer>
    <p class="text-center">made with love of RE by <a href="https://twitter.com/sar5430" target="_blank">sar</a> with the great <a href="https://github.com/josephspurrier/gowebapp">gowebapp</a><br>design made by the sure guy <a href="https://twitter.com/mpgn_x64" target="_blank">Bonclay</a>, inspired by <a href="https://hackthebox.eu" target="_blank">hackthebox.eu</a><br>You can support the cost of crackmes.one infrastructure <a href="https://www.buymeacoffee.com/sar5430">here</a></p>
</footer>



        

    

