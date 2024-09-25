import { v } from "../../../index";
import { Link } from "react-router-dom";
import { Breadcrumbs, BreadcrumbItem } from "@nextui-org/react";

// eslint-disable-next-line react/prop-types
export const Breadcrumb = ({ pageName }) => {
  return (
    <>
      <div className="px-5">
        <div className="flex flex-row justify-between">
          <span className="text-4xl font-bold text-gray-800 ">{pageName}</span>

          <Breadcrumbs>
            <BreadcrumbItem>
              <Link className="font-medium" to="/home">
                <span>Home</span>
              </Link>
            </BreadcrumbItem>
            <BreadcrumbItem>{pageName}</BreadcrumbItem>
          </Breadcrumbs>
        </div>
        <div className={`h-2 ${v.bg_green_sena}  inline-block w-full`}></div>
      </div>
    </>
  );
};
