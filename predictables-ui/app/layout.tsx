import type { Metadata } from 'next';
import './globals.css';
// import Navbar from '@components/Navbar';
import Navbar from '@components/NavbarDaisy';
import Drawer from '@components/Drawer';

export const metadata: Metadata = {
  title: 'PredicTables',
  description: 'PredicTables Web Client',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body
        className={`
        bg-white text-black
        flex flex-col w-[100vw] h-[100vh] justify-center items-center `}
      >
        <Navbar />
        {/* <div id="mainContainer" className={`mt-[120px] w-[80%] h-[90%]`}>
          <Drawer /> */}
        <main className="h-full w-full">{children}</main>
        {/* </div> */}
      </body>
    </html>
  );
}
