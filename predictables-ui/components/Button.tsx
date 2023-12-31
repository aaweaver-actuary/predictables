import React, { ReactNode } from 'react';

interface ButtonProps {
  children: ReactNode;
  onClick?: () => void;
  filledIn?: boolean;
  clickable?: boolean;
  selected?: boolean;
  inactive?: boolean;
}

const Button = ({
  children,
  onClick,
  filledIn = false,
  clickable = true,
  selected = false,
  inactive = false,
}: ButtonProps) => {
  // Will fill the button in one of two ways:
  // 1. If the button HAS the filledIn design, it will be filled in when it is NOT selected
  // 2. If the button DOES NOT HAVE the filledIn design, it will be filled in when it IS selected
  const filled = (filledIn && !selected) || (!filledIn && selected);
  return (
    <button
      onClick={onClick}
      className={`
      rounded-sm delay-100 justify-center items-center p-2 mx-2 min-w-[90px] w-fit h-[55px] text-lg duration-100 font-normal
      select-none
      ${clickable ? 'cursor-default active:scale-90' : ''}
      ${
        filled
          ? `bg-black text-white hover:bg-white hover:text-black shadow-lg border-black border-[2px]`
          : `bg-white text-black hover:bg-black hover:text-white shadow-lg border-black border-[2px]`
      }
      ${inactive ? 'opacity-50 cursor-not-allowed' : ''}
    `}
    >
      {children}
    </button>
  );
};

export default Button;
